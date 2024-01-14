from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    assert encrypt_message("text", 6) == "txet"

    assert encrypt_message("text", 1) == "t_txe"

    assert encrypt_message("text", 2) == "tx_et"

    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("text", '1')
    pass
