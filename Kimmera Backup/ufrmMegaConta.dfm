object frmMegaConta: TfrmMegaConta
  Left = 0
  Top = 0
  BorderIcons = [biSystemMenu]
  BorderStyle = bsSingle
  Caption = 'Mega Conta'
  ClientHeight = 74
  ClientWidth = 420
  Color = clBtnFace
  Font.Charset = DEFAULT_CHARSET
  Font.Color = clWindowText
  Font.Height = -11
  Font.Name = 'Tahoma'
  Font.Style = []
  OldCreateOrder = False
  Position = poDesktopCenter
  OnShow = FormShow
  PixelsPerInch = 96
  TextHeight = 13
  object Label1: TLabel
    Left = 8
    Top = 13
    Width = 28
    Height = 13
    Caption = 'E-mail'
  end
  object Label2: TLabel
    Left = 207
    Top = 13
    Width = 30
    Height = 13
    Caption = 'Senha'
  end
  object edtEmail: TcxDBTextEdit
    Left = 8
    Top = 32
    DataBinding.DataField = 'EMAIL'
    DataBinding.DataSource = dsMega
    TabOrder = 0
    Width = 193
  end
  object edtSenha: TcxDBTextEdit
    Left = 207
    Top = 32
    DataBinding.DataField = 'SENHA'
    DataBinding.DataSource = dsMega
    Properties.EchoMode = eemPassword
    TabOrder = 1
    Width = 121
  end
  object btn1: TButton
    Left = 334
    Top = 30
    Width = 75
    Height = 25
    Caption = 'Gravar'
    TabOrder = 2
    OnClick = btn1Click
  end
  object dsMega: TUniDataSource
    DataSet = frmPrincipal.tMega
    Left = 248
    Top = 40
  end
end
