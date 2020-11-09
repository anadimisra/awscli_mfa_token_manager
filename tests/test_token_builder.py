import pytest
from awscli_mfa_token_manager.token_data_builder import TokenDataBuilder
from configparser import ConfigParser
from pathlib import Path


def test_builds_mfa_serial_token_from_arg(tmp_path):
    builder = TokenDataBuilder()
    config = ConfigParser()
    config["default"] = {
        "region": "us-east-1",
        "output": "json",
        "mfa_serial": "123"
    }
    build_config(tmp_path, config)
    credentials_data = builder.with_credentials_directory(tmp_path)
    assert Path(credentials_data.get_token_builder_data()["credentials_dir"]) == tmp_path


def test_uses_existing_serial_number_if_exists(tmp_path):
    config = ConfigParser()
    config["default"] = {
        "region": "us-east-1",
        "output": "json",
        "mfa_serial": "123"
    }
    build_config(tmp_path, config)
    token_data = TokenDataBuilder().with_profile("default").with_credentials_directory(tmp_path).with_serial_number(
        None).get_token_builder_data()
    assert token_data["mfa_serial"] == "123"

def test_sys_exit_error_on_missing_mfa_serial_(tmp_path):
    config = ConfigParser()
    config["default"] = {
        "region": "us-east-1",
        "output": "json"
    }
    build_config(tmp_path, config)
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        token_data = TokenDataBuilder().with_profile("default").with_credentials_directory(tmp_path).with_serial_number(
        None).get_token_builder_data()
    assert pytest_wrapped_e.type == SystemExit

def test_serial_number_arg_overwrites_mfa_serial(tmp_path):
    config = ConfigParser()
    config["foo"] = {
        "mfa_serial": "123"
    }
    build_config(tmp_path, config)
    token_data = TokenDataBuilder().with_profile("foo").with_credentials_directory(
        str(tmp_path)).with_serial_number("456").get_token_builder_data()
    assert token_data["mfa_serial"] == "456", "serial number argument overwrites value read from config file"

def build_config(tmp_path, config):
    config_file = tmp_path / "config"
    with open(str(config_file), 'w+') as cf:
        config.write(cf)