#Boa:Frame:Frame1

import datetime
import wx, MySQLdb

conn=MySQLdb.connect(host="localhost",user="root",passwd="",db="akses_database")
cur = conn.cursor()


# Ambil Tanggal Hari ini
skrg = datetime.date.today()
# Ambil Hari
day = skrg.day
# Ambil Bulan
month = skrg.month
# Ambil Tahun
year = skrg.year


def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1PANEL1, wxID_FRAME1STATICTEXT1, 
 wxID_FRAME1STATICTEXT2, wxID_FRAME1STATICTEXT3, wxID_FRAME1TGL_DAFTAR, 
 wxID_FRAME1TGL_LAHIR, wxID_FRAME1TMB_BERSIH, wxID_FRAME1TMB_HAPUS, 
 wxID_FRAME1TMB_SIMPAN, wxID_FRAME1TXT_NAMA, 
] = [wx.NewId() for _init_ctrls in range(11)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(487, 252), size=wx.Size(400, 248),
              style=wx.DEFAULT_FRAME_STYLE, title='Operasi Data Tanggal')
        self.SetClientSize(wx.Size(384, 210))

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(384, 210),
              style=wx.TAB_TRAVERSAL)

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label='Nama', name='staticText1', parent=self.panel1,
              pos=wx.Point(32, 24), size=wx.Size(28, 13), style=0)

        self.txt_nama = wx.TextCtrl(id=wxID_FRAME1TXT_NAMA, name='txt_nama',
              parent=self.panel1, pos=wx.Point(144, 24), size=wx.Size(100, 21),
              style=wx.TE_PROCESS_ENTER, value='')
        self.txt_nama.Bind(wx.EVT_TEXT_ENTER, self.OnTxt_namaTextEnter,
              id=wxID_FRAME1TXT_NAMA)

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
              label='Tanggal Lahir', name='staticText2', parent=self.panel1,
              pos=wx.Point(32, 64), size=wx.Size(65, 13), style=0)

        self.tgl_lahir = wx.DatePickerCtrl(id=wxID_FRAME1TGL_LAHIR,
              name='tgl_lahir', parent=self.panel1, pos=wx.Point(144, 56),
              size=wx.Size(96, 21), style=wx.DP_SHOWCENTURY)
        self.tgl_lahir.SetLabel('')
        self.tgl_lahir.SetValue(wx.DateTimeFromDMY(24, 2, 2012, 0, 0, 0))
        self.tgl_lahir.SetHelpText('')

        self.tmb_simpan = wx.Button(id=wxID_FRAME1TMB_SIMPAN, label='Simpan',
              name='tmb_simpan', parent=self.panel1, pos=wx.Point(40, 152),
              size=wx.Size(75, 23), style=0)
        self.tmb_simpan.Bind(wx.EVT_BUTTON, self.OnTmb_simpanButton,
              id=wxID_FRAME1TMB_SIMPAN)

        self.tmb_bersih = wx.Button(id=wxID_FRAME1TMB_BERSIH, label='Bersih',
              name='tmb_bersih', parent=self.panel1, pos=wx.Point(152, 152),
              size=wx.Size(75, 23), style=0)
        self.tmb_bersih.Bind(wx.EVT_BUTTON, self.OnTmb_bersihButton,
              id=wxID_FRAME1TMB_BERSIH)

        self.tmb_hapus = wx.Button(id=wxID_FRAME1TMB_HAPUS, label='Hapus',
              name='tmb_hapus', parent=self.panel1, pos=wx.Point(272, 152),
              size=wx.Size(75, 23), style=0)
        self.tmb_hapus.Bind(wx.EVT_BUTTON, self.OnTmb_hapusButton,
              id=wxID_FRAME1TMB_HAPUS)

        self.staticText3 = wx.StaticText(id=wxID_FRAME1STATICTEXT3,
              label='Tanggal Daftar', name='staticText3', parent=self.panel1,
              pos=wx.Point(32, 104), size=wx.Size(73, 13), style=0)

        self.tgl_daftar = wx.TextCtrl(id=wxID_FRAME1TGL_DAFTAR,
              name='tgl_daftar', parent=self.panel1, pos=wx.Point(144, 96),
              size=wx.Size(100, 21), style=0, value='')

    def __init__(self, parent):
        self._init_ctrls(parent)
        ## Menampilkan Tanggal Hari ini
        # Tampilkan ke dalam textctrl tgl_daftar
        self.tgl_daftar.SetValue("%02d/%02d/%4d"%(day, month, year))

    def Bersih(self) :
        self.txt_nama.SetValue("")
        self.tgl_lahir.SetValue("%02d/%02d/%4d" % (day, month, year))
    def OnTmb_simpanButton(self, event):
        
        sql = " select * from operasi_tanggal where nama \
        = '%s'" %(self.txt_nama.GetValue())
        cur.execute(sql)
        hasil= cur.fetchone()
        
        selected = self.tgl_lahir.GetValue()
        month_lahir = selected.Month + 1
        day_lahir = selected.Day
        year_lahir = selected.Year

        tgl_lahir1 = datetime.date(year_lahir,month_lahir,day_lahir)
        
        tgl_daftar1 = datetime.date(year,month,day)
        if cur.rowcount > 0 :
            sql =" update operasi_tanggal set tgl_lahir =\
            '%s', tgl_daftar='%s' where nama ='%s'"%\
            (tgl_lahir1,\
            tgl_daftar1,self.txt_nama.GetValue())
        else :
            sql ="insert into operasi_tanggal (nama,tgl_lahir,tgl_daftar) \
            values ('%s','%s','%s')"%(self.txt_nama.GetValue(),\
            tgl_lahir1,tgl_daftar1)
        cur.execute(sql)
        self.Bersih()

    def OnTmb_bersihButton(self, event):
        self.Bersih()

    def OnTmb_hapusButton(self, event):
        if  self.txt_nama.GetValue()=="" :
            self.pesan = wx.MessageDialog\
            (self,"Nama belum diisi","Konfirmasi",wx.OK)
            self.pesan.ShowModal()
            event.Skip()
        sql = " select * from operasi_tanggal where nama \
        = '%s'" % (self.txt_nama.GetValue())
        cur.execute(sql)
        hasil= cur.fetchone()
        if cur.rowcount>0 :
            tanya = wx.MessageDialog(self,\
            message="Anda Yakin Hendak Menghapus Nama"\
            +" "+self.txt_nama.GetValue()\
            ,style = wx.YES_NO)
            if tanya.ShowModal()==wx.ID_YES:
                sql = "delete from operasi_tanggal where nama \
                = '%s'" % (self.txt_nama.GetValue())
                cur.execute(sql)
        else :
            self.pesan = wx.MessageDialog(self,\
            "Nama yang akan dihapus tidak terdata\
            di database","Konfirmasi",wx.OK)
            self.pesan.ShowModal()

    def OnTxt_namaTextEnter(self, event):
        sql = " select * from operasi_tanggal where nama \
        = '%s'" %(self.txt_nama.GetValue())
        cur.execute(sql)
        hasil= cur.fetchone()
        if cur.rowcount > 0 :
            python_birthdate = hasil[1]
            day = python_birthdate.day
            month = python_birthdate.month
            year = python_birthdate.year
            displayed_birthday = wx.DateTimeFromDMY(day,month-1,year)
            self.tgl_lahir.SetValue(displayed_birthday)
            tgl_daftar1 = hasil[2]
            day1 = tgl_daftar1.day
            month1 = tgl_daftar1.month
            year1 = tgl_daftar1.year
            displayed_birthday1 = wx.DateTimeFromDMY(day1,month1-1,year1)
            self.tgl_daftar.SetValue(displayed_birthday1)
        else :
            self.pesan = wx.MessageDialog(self,\
            "Data Tidak Ada","Konfirmasi",wx.OK)
            self.pesan.ShowModal()

