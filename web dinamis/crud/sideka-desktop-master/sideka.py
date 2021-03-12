#!/usr/bin/env python

import wx
import frm_sideka_menu

modules ={u'bantuan': [0, u'bantuan', u'bantuan.py'],
 u'cari_administrasi': [0, '', u'cari_administrasi.py'],
 u'cari_kemiskinan': [0, '', u'cari_kemiskinan.py'],
 u'cari_penduduk': [0, '', u'cari_penduduk.py'],
 u'data_penduduk': [0, '', u'data_penduduk.py'],
 u'edit_administrasi_surat': [0, '', u'edit_administrasi_surat.py'],
 u'edit_data_kemiskinan': [0, '', u'edit_data_kemiskinan.py'],
 u'frm_sideka_menu': [1, 'Main frame of Application', u'frm_sideka_menu.py'],
 u'input_administrasi_surat': [0, '', u'input_administrasi_surat.py'],
 u'input_data_kemiskinan': [0, '', u'input_data_kemiskinan.py'],
 u'input_indikator_kemiskinan': [0, '', u'input_indikator_kemiskinan.py'],
 u'kk_sementara': [0, '', u'kk_sementara.py'],
 u'kk_tetap': [0, '', u'kk_tetap.py'],
 u'laporan_administrasi': [0, '', u'laporan_administrasi.py'],
 u'laporan_kemiskinan': [0, '', u'laporan_kemiskinan.py'],
 u'laporan_penduduk': [0, '', u'laporan_penduduk.py'],
 u'laporan_potensi': [0, '', u'laporan_potensi.py'],
 u'laporan_profil': [0, '', u'laporan_profil.py'],
 u'laporan_statistik': [0, '', u'laporan_statistik.py'],
 u'login_edit_kemiskinan': [0, '', u'login_edit_kemiskinan.py'],
 u'login_edit_penduduk': [0, '', u'login_edit_penduduk.py'],
 u'login_edit_profil': [0, '', u'login_edit_profil.py'],
 u'login_edit_surat': [0, '', u'login_edit_surat.py'],
 u'login_ekonomi': [0, '', u'login_ekonomi.py'],
 u'login_indikator_kemiskinan': [0, '', u'login_indikator_kemiskinan.py'],
 u'login_input_kemiskinan': [0, '', u'login_input_kemiskinan.py'],
 u'login_input_penduduk': [0, '', u'login_input_penduduk.py'],
 u'login_input_profil': [0, '', u'login_input_profil.py'],
 u'login_input_surat': [0, '', u'login_input_surat.py'],
 u'login_inventaris_desa': [0, '', u'login_inventaris_desa.py'],
 u'login_lahan': [0, '', u'login_lahan.py'],
 u'login_pariwisata': [0, '', u'login_pariwisata.py'],
 u'login_pecah_keluarga': [0, '', u'login_pecah_keluarga.py'],
 u'login_tambak': [0, '', u'login_tambak.py'],
 u'peringatan': [0, '', u'peringatan.py'],
 u'statistik_administrasi': [0, '', u'statistik_administrasi.py'],
 u'statistik_kemiskinan': [0, '', u'statistik_kemiskinan.py'],
 u'statistik_penduduk': [0, '', u'statistik_penduduk.py'],
 u'statistik_potensi': [0, '', u'statistik_potensi.py'],
 u'tambah_kk_sementara': [0, '', u'tambah_kk_sementara.py'],
 u'tambah_kk_tetap': [0, '', u'tambah_kk_tetap.py'],
 u'tambah_penduduk': [0, '', u'tambah_penduduk.py']}

class SiDeKa(wx.App):
    def OnInit(self):
        self.main = frm_sideka_menu.create(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True

def main():
    application = SiDeka(0)
    application.MainLoop()

if __name__ == '__main__':
    main()
