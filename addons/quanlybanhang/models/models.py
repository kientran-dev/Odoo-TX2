# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Hang(models.Model):
    _name = 'hang'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hãng sản xuất'

    tenhang = fields.Char(string="Tên hãng", required=True, tracking=True)
    mahang = fields.Integer(string="Mã hãng", required=True, tracking=True)
    diachi = fields.Char(string="Địa chỉ", required=True, tracking=True)
    sodt = fields.Char(string="Số điện thoại", required=True, tracking=True)

    _sql_constraints = [
        ('mahang_unique', 'unique(mahang)', 'Mã hãng không được trùng!')
    ]

class NhanVien(models.Model):
    _name = 'nhanvien'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Nhân viên'

    tennv = fields.Char(string="Họ và tên", required=True, tracking=True)
    manv = fields.Integer(string="Mã nhân viên", required=True, tracking=True)
    gioitinh = fields.Selection([('Nam', 'Nam'), ('Nữ', 'Nữ')], string="Giới tính", tracking=True)
    sdt = fields.Char(string="Số điện thoại", tracking=True)

    _sql_constraints = [
        ('manv_unique', 'unique(manv)', 'Mã nhân viên không được trùng!')
    ]

class SanPham(models.Model):
    _name = 'sanpham'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Sản phẩm'

    masp = fields.Char(string="Mã sản phẩm", required=True, tracking=True)
    tensp = fields.Char(string="Tên sản phẩm", required=True, tracking=True)
    soluong = fields.Integer(string="Số lượng", required=True, tracking=True)
    giaban = fields.Integer(string="Giá bán", required=True, tracking=True)
    mausac = fields.Selection([('Xanh', 'Xanh'), ('Đỏ', 'Đỏ'), ('Vàng', 'Vàng')], string="Màu sắc", tracking=True)

    _sql_constraints = [
        ('masp_unique', 'unique(masp)', 'Mã sản phẩm không được trùng!')
    ]
