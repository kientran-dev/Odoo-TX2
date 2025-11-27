# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Hang(models.Model):
    _name = 'hang'

    tenhang = fields.Char(string="Tên hãng", required=True)
    mahang = fields.Integer(string="Mã hãng", required=True)
    diachi = fields.Char(string="Địa chỉ", required=True)
    sodt = fields.Char(string="Số điện thoại", required=True)

class NhanVien(models.Model):
    _name = 'nhanvien'

    tennv = fields.Char(string="Họ và tên", required=True)
    manv = fields.Integer(string="Mã nhân viên", required=True)
    gioitinh = fields.Selection([('Nam', 'Nam'), ('Nữ', 'Nữ')], string="Giới tính")
    sdt = fields.Char(string="Số điện thoại")

class SanPham(models.Model):
    _name = 'sanpham'

    masp = fields.Char(string="Mã sản phẩm", required=True)
    tensp = fields.Char(string="Tên sản phẩm", required=True)
    soluong = fields.Integer(string="Số lượng", required=True)
    giaban = fields.Integer(string="Giá bán", required=True)
    mausac = fields.Selection([('Xanh', 'Xanh'), ('Đỏ', 'Đỏ'), ('Vàng', 'Vàng')], string="Màu sắc")
