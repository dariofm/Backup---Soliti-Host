unit ufrmPrincipal;

interface

uses
  Winapi.Windows, Winapi.Messages, System.SysUtils, System.Variants, System.Classes, Vcl.Graphics,
  Vcl.Controls, Vcl.Forms, Vcl.Dialogs, Vcl.StdCtrls, Data.DB, DBAccess, Uni,
  Vcl.Grids, Vcl.DBGrids, MemDS, UniProvider, SQLiteUniProvider, cxGraphics,
  cxControls, cxLookAndFeels, cxLookAndFeelPainters, cxContainer, cxEdit,
  cxTextEdit, cxMaskEdit, cxSpinEdit, cxTimeEdit, System.ImageList, Vcl.ImgList,
  cxImageList, cxDBEdit, Vcl.ExtCtrls, Vcl.AppEvnts,System.IniFiles, Vcl.Menus,
  InterBaseUniProvider;

type
  TfrmPrincipal = class(TForm)
    dlgOpen1: TOpenDialog;
    btnArquivo: TButton;
    btn2: TButton;
    SQLiteUniProvider1: TSQLiteUniProvider;
    UniConnection1: TUniConnection;
    qArquivos: TUniQuery;
    dbgrd1: TDBGrid;
    qArquivosID: TIntegerField;
    qArquivosDESCRICAO: TStringField;
    dsArquivo: TUniDataSource;
    qArquivosTIPO: TStringField;
    btnRemover: TButton;
    qTarefa: TUniQuery;
    dbgrd2: TDBGrid;
    qTarefaID: TIntegerField;
    qTarefaTIME: TTimeField;
    dsTarefa: TUniDataSource;
    edtTime: TcxTimeEdit;
    btnAddTarefa: TButton;
    btn1: TButton;
    cxImageList1: TcxImageList;
    Label1: TLabel;
    Label2: TLabel;
    tEmpresa: TUniTable;
    tEmpresaDESCRICAO: TStringField;
    tEmpresaCNPJ: TStringField;
    edtEmpresa: TcxDBTextEdit;
    dsEmpresa: TUniDataSource;
    btn3: TButton;
    edtCnpj: TcxDBSpinEdit;
    Label3: TLabel;
    Label4: TLabel;
    btnRemoverLocal: TButton;
    btnDiretorioDestino: TButton;
    dbgrd3: TDBGrid;
    tDestino: TUniTable;
    tDestinoID: TIntegerField;
    tDestinoDIRETORIO: TStringField;
    dsDestino: TUniDataSource;
    tmrDisparador: TTimer;
    hora: TLabel;
    btn4: TButton;
    tMega: TUniTable;
    tMegaEMAIL: TStringField;
    tMegaSENHA: TStringField;
    qArquivosDIRETORIO: TStringField;
    TrayIcon1: TTrayIcon;
    ApplicationEvents1: TApplicationEvents;
    tmrAutoMinimiza: TTimer;
    btn5: TButton;
    pm1: TPopupMenu;
    Host1: TMenuItem;
    Soliti1: TMenuItem;
    qGen: TUniQuery;
    uConFire: TUniConnection;
    InterBaseUniProvider1: TInterBaseUniProvider;
    qEmit: TUniQuery;
    procedure btnArquivoClick(Sender: TObject);
    procedure btn2Click(Sender: TObject);
    procedure btnRemoverClick(Sender: TObject);
    procedure btnAddTarefaClick(Sender: TObject);
    procedure btn1Click(Sender: TObject);
    procedure FormShow(Sender: TObject);
    procedure btn3Click(Sender: TObject);
    procedure btnDiretorioDestinoClick(Sender: TObject);
    procedure btnRemoverLocalClick(Sender: TObject);
    procedure tmrDisparadorTimer(Sender: TObject);
    procedure btn4Click(Sender: TObject);
    procedure ApplicationEvents1Minimize(Sender: TObject);
    procedure TrayIcon1Click(Sender: TObject);
    procedure tmrAutoMinimizaTimer(Sender: TObject);
    procedure btn5Click(Sender: TObject);
    procedure edtEmpresaExit(Sender: TObject);
    procedure edtCnpjExit(Sender: TObject);
    procedure Host1Click(Sender: TObject);
    procedure Soliti1Click(Sender: TObject);
    procedure FormClose(Sender: TObject; var Action: TCloseAction);
  private
    { Private declarations }
  public
    { Public declarations }
    procedure WizardArq(Tipo:string);
  end;

var
  frmPrincipal: TfrmPrincipal;

implementation

uses
  ufrmMegaConta;

{$R *.dfm}

procedure TfrmPrincipal.btnAddTarefaClick(Sender: TObject);
begin
  qTarefa.Insert;
  qTarefaTIME.AsString      := edtTime.Text;
  qTarefa.Post;

  edtEmpresa.SetFocus;
end;

procedure TfrmPrincipal.btnArquivoClick(Sender: TObject);
begin
if dlgOpen1.Execute then
begin
  qArquivos.Insert;
  qArquivosDESCRICAO.AsString := dlgOpen1.FileName;
  qArquivosTIPO.AsString      := '1';
  qArquivos.Post;
end;

  edtEmpresa.SetFocus;
end;

procedure TfrmPrincipal.btnDiretorioDestinoClick(Sender: TObject);
begin
with TFileOpenDialog.Create(nil) do
  try
    Options := [fdoPickFolders];
    if Execute then
    begin
      tDestino.Insert;
      tDestinoDIRETORIO.AsString := FileName;

      tDestino.Post;
    end;
  finally
    Free;
  end;


  edtEmpresa.SetFocus;
end;

procedure TfrmPrincipal.btnRemoverClick(Sender: TObject);
begin
  if qArquivos.RecordCount > 0 then
  begin
    qArquivos.Delete;
  end;
  edtEmpresa.SetFocus;
end;

procedure TfrmPrincipal.btnRemoverLocalClick(Sender: TObject);
begin
  if tDestino.RecordCount > 0 then
  begin
    tDestino.Delete;
  end;

  edtEmpresa.SetFocus;
end;

procedure TfrmPrincipal.edtCnpjExit(Sender: TObject);
begin
  if tEmpresa.State in [dsEdit] then
    tEmpresa.Post;


end;

procedure TfrmPrincipal.edtEmpresaExit(Sender: TObject);
begin
  if tEmpresa.State in [dsEdit] then
    tEmpresa.Post;


end;

procedure TfrmPrincipal.FormClose(Sender: TObject; var Action: TCloseAction);
begin
  if messagebox(frmPrincipal.Handle,'Confirmar sa?da do Sistema?','Sair',mb_yesno+MB_ICONQUESTION)= idno then
  begin
    Abort
  end
    else
      begin
        frmPrincipal.Free;
        frmPrincipal := nil;
        Application.Terminate;
      end;
end;

procedure TfrmPrincipal.FormShow(Sender: TObject);
begin
  qTarefa.Open;
  qArquivos.Open;
  tEmpresa.Open;
  tMega.Open;
  tDestino.Open;

  tEmpresa.Edit;
end;

procedure TfrmPrincipal.Host1Click(Sender: TObject);
begin
  WizardArq('Host');
end;

procedure TfrmPrincipal.Soliti1Click(Sender: TObject);
begin
  WizardArq('Soliti');
end;

procedure TfrmPrincipal.tmrAutoMinimizaTimer(Sender: TObject);
begin
  Self.Hide();
  Self.WindowState := wsMinimized;
  TrayIcon1.Visible := True;
  TrayIcon1.Animate := True;
  TrayIcon1.ShowBalloonHint;

  tmrAutoMinimiza.Enabled := False;
end;

procedure TfrmPrincipal.tmrDisparadorTimer(Sender: TObject);
begin
  hora.caption := timetostr(time);

  qTarefa.First;
  while not qTarefa.Eof do
  begin

    if qTarefaTIME.AsString = hora.caption then
    begin


      WinExec('C:\Kimmera Backup\app\run.bat',SW_HIDE);

    end;


    qTarefa.Next;
  end;

end;

procedure TfrmPrincipal.TrayIcon1Click(Sender: TObject);
begin
  TrayIcon1.Visible := False;
  Show();
  WindowState := wsNormal;
  Application.BringToFront();
end;

procedure TfrmPrincipal.WizardArq(Tipo: string);
var
  config:TIniFile;
  banco,ip_servidor,xmlNFe,xmlNfce:string;
  fantasia,cnpj:string;
begin
  qGen.SQL.Clear;
  qGen.SQL.Text := 'delete from ARQUIVOS';
  qGen.ExecSQL;

  qArquivos.Refresh;

  if messagebox(frmPrincipal.Handle,'Definir a hora atual para o Backup?','Confirmar',mb_yesno+MB_ICONQUESTION)= idyes then
  begin

  qGen.SQL.Clear;
  qGen.SQL.Text := 'delete from TAREFA';
  qGen.ExecSQL;

  qTarefa.Refresh;

  qTarefa.Insert;
  qTarefaTIME.AsDateTime      := now;
  qTarefa.Post;

  end;

  if Tipo = 'Host' then
  begin
  try
    try

      config := TIniFile.Create('C:\TSD\Host\Conexao.ini');
      banco := config.ReadString('CONEXAO','RETAGUARDA','');
      ip_servidor := config.ReadString('CONEXAO','IP_SERVIDOR','');

      uConFire.Connected := False;
      uConFire.Server := ip_servidor;
      uConFire.Database :=  banco;     
      uConFire.Connected := True;   
      
      qEmit.Close;      
      qEmit.SQL.Clear;
      qEmit.SQL.Text := 'select FANTASIA,CNPJ from EMITENTE';
      qEmit.Open;    
 
      fantasia   := qEmit.FieldByName('FANTASIA').AsString; 
      cnpj       := qEmit.FieldByName('CNPJ').AsString; 

      tEmpresa.Edit;
      tEmpresaDESCRICAO.AsString := fantasia;
      tEmpresaCNPJ.AsString := cnpj;      
      tEmpresa.Post;
      
          
      qArquivos.Insert;
      qArquivosDESCRICAO.AsString := banco;
      qArquivosTIPO.AsString      := '1';
      qArquivos.Post;

      qArquivos.Insert;
      qArquivosDESCRICAO.AsString := 'C:\TSD\Host\XML_NFCe';
      qArquivosTIPO.AsString      := '0';
      qArquivosDIRETORIO.AsString := 'XML_NFCe';
      qArquivos.Post;

      qArquivos.Insert;
      qArquivosDESCRICAO.AsString := 'C:\TSD\Host\XML';
      qArquivosTIPO.AsString      := '0';
      qArquivosDIRETORIO.AsString := 'XML';
      qArquivos.Post;

    finally
      config.Free;
    end; 
    except
      ShowMessage('Sistema n?o encontrado, fazer a configura??o manualmente.');
    end;
  end;

  if Tipo = 'Soliti' then
  begin
  try
    try

      config := TIniFile.Create('C:\Soliti\App\Config.ini');
      banco := config.ReadString('DATABASE','LOCAL','')+config.ReadString('DATABASE','BASE','');

      qArquivos.Insert;
      qArquivosDESCRICAO.AsString := banco;
      qArquivosTIPO.AsString      := '1';
      qArquivos.Post;

      uConFire.Connected := False;
      uConFire.Server := ip_servidor;
      uConFire.Database :=  banco;     
      uConFire.Connected := True;   
      
      qEmit.Close;      
      qEmit.SQL.Clear;
      qEmit.SQL.Text := 'select FANTASIA,CGC_CNPJ from LOJA';
      qEmit.Open;    
 
      fantasia   := qEmit.FieldByName('FANTASIA').AsString; 
      cnpj       := StringReplace(StringReplace(StringReplace(qEmit.FieldByName('CGC_CNPJ').AsString, '.', '', [rfReplaceAll]), '-', '', [rfReplaceAll]), '/', '', [rfReplaceAll]);       

      tEmpresa.Edit;
      tEmpresaDESCRICAO.AsString := fantasia;
      tEmpresaCNPJ.AsString := cnpj;      
      tEmpresa.Post;
      
    finally
      config.Free;
    end;
    except
      ShowMessage('Sistema n?o encontrado, fazer a configura??o manualmente.');
    end;
  end;


end;

procedure TfrmPrincipal.ApplicationEvents1Minimize(Sender: TObject);
begin
  if tEmpresa.State in [dsEdit] then
    tEmpresa.Post;


  Self.Hide();
  Self.WindowState := wsMinimized;
  TrayIcon1.Visible := True;
  TrayIcon1.Animate := True;
  TrayIcon1.ShowBalloonHint;
end;

procedure TfrmPrincipal.btn1Click(Sender: TObject);
begin
  if qTarefa.RecordCount > 0 then
    qTarefa.Delete;

  edtEmpresa.SetFocus;
end;

procedure TfrmPrincipal.btn2Click(Sender: TObject);
var
    Filepath : string ;
begin
with TFileOpenDialog.Create(nil) do
  try
    Options := [fdoPickFolders];
    if Execute then
    begin
      qArquivos.Insert;
      qArquivosDESCRICAO.AsString := FileName;
      qArquivosTIPO.AsString      := '0';
      qArquivosDIRETORIO.AsString := ExtractFileName(FileName);
      qArquivos.Post;
    end;
  finally
    Free;
  end;

  edtEmpresa.SetFocus;
end;

procedure TfrmPrincipal.btn3Click(Sender: TObject);
begin
  if tEmpresa.State in [dsEdit] then
    tEmpresa.Post;

  edtEmpresa.SetFocus;
end;

procedure TfrmPrincipal.btn4Click(Sender: TObject);
var
Resposta,senha : string;
begin
// Perguntando qual e a sua cidade

  senha := StringReplace(DateToStr(Date),'/','',[rfReplaceAll, rfIgnoreCase]);




  Resposta := InputBox('Pergunta', #31+'Senha:','');

  if (Resposta <> '') and (Resposta = senha)  then
  begin
    frmMegaConta.ShowModal;
  end;



end;

procedure TfrmPrincipal.btn5Click(Sender: TObject);
begin
  if tEmpresa.State in [dsEdit] then
    tEmpresa.Post;

  edtEmpresa.SetFocus;

  WinExec('C:\Kimmera Backup\app\run.bat',SW_NORMAL);
end;

end.
