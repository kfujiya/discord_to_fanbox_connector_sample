# discord to fanbox connector

## 1. �T�v
���F��discord�T�[�o�ɂ��āA�Q���҂̎���������s���A�v���P�[�V�����ł��B
�m�l�̈˗������Ƃɍ\�z���̂��̂ɂȂ�܂��B
���l�^�͂䂫�݂��̂���̃A�C�f�A�ł�: https://note.com/fujii_shino/n/n5f1d6f057db4

## 2. �K�v�Ȃ���
* python 3.9�ȏ�
  - https://www.python.jp/install/windows/install.html
  - https://qiita.com/shun_sakamoto/items/7944d0ac4d30edf91fde
* python���C�u����(���z���ɃC���X�g�[������Ƃ悢)
  - Helium
  - requests
  - discord.py

* pixiv FANBOX�A�J�E���g
  - ���[�U��, �p�X���[�h

* discord�T�[�o
  - �T�[�oID
  - discord�A�v���P�[�V�����̃N���C�A���gID, �V�[�N���b�g�R�[�h, �A�v���P�[�V�����R�[�h( https://apidog.com/jp/blog/discord-api/ )

## 3. ��Ɠ��e
* ���̃��|�W�g�����N���[������
* pixiv FANBOX�A�J�E���g��discord�̏���secret.ini�ɏ�������
* �R�}���h�ŃR�l�N�^�[�����s����
  - `\.venv\Scripts\activate`
  - `python pixivConnectorBatch.py`

* bot�`���Ŏ��s��������(�T�[�o�[��bot��o�^���Ă���A����secret.ini��bot���Ăяo��token���L�ڂ���K�v����)
  - `\.venv\Scripts\activate`
  - `python pixivConnectorBot.py`