unit ufrmMegaConta;

interface

uses
  Winapi.Windows, Winapi.Messages, System.SysUtils, System.Variants, System.Classes, Vcl.Graphics,
  Vcl.Controls, Vcl.Forms, Vcl.Dialogs, cxGraphics, cxControls, cxLookAndFeels,
  cxLookAndFeelPainters, cxContainer, cxEdit, Data.DB, DBAccess, Uni,
  Vcl.StdCtrls, cxTextEdit, cxDBEdit;

type
  TfrmMegaConta = class(TForm)
    edtEmail: TcxDBTextEdit;
    edtSenha: TcxDBTextEdit;
    Label1: TLabel;
    Label2: TLabel;
    btn1: TButton;
    dsMega: TUniDataSource;
    procedure FormShow(Sender: TObject);
    procedure btn1Click(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  frmMegaConta: TfrmMegaConta;

implementation

uses
  ufrmPrincipal;

{$R *.dfm}

procedure TfrmMegaConta.btn1Click(Sender: TObject);
begin
  if frmPrincipal.tMega.State in [dsEdit] then
    frmPrincipal.tMega.Post;
    Close;
end;

procedure TfrmMegaConta.FormShow(Sender: TObject);
begin
  frmPrincipal.tMega.Edit;
end;

end.
