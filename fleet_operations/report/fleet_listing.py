# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.

try:
    from odoo.addons.report_xlsx.report.report_xlsx import ReportXlsx
except ImportError:
    class ReportXlsx(object):
        def __init__(self, *args, **kwargs):
            pass


class FleetListing(ReportXlsx):

    def get_heading(self):
        head_title = {'name': '',
                      'rev_no': '',
                      'doc_no': '',
                      }
        head_object = self.env['report.heading']
        head_ids = head_object.search([], order='id')
        if head_ids:
            head_rec = head_ids[0]
            if head_rec:
                head_title['name'] = head_rec.name or ''
                head_title['rev_no'] = head_rec.revision_no or ''
                head_title['doc_no'] = head_rec.document_no or ''
                head_title['image'] = head_rec.image or ''
        return head_title

    def generate_xlsx_report(self, workbook, data, fleet_listing):
        worksheet = workbook.add_worksheet('fleet_listing')
        worksheet.set_column(0, 0, 10)
        worksheet.set_column(1, 1, 25)
        worksheet.set_column(2, 2, 10)
        worksheet.set_column(3, 3, 15)
        worksheet.set_column(4, 4, 10)
        worksheet.set_column(5, 5, 12)
        worksheet.set_column(6, 6, 15)
        worksheet.set_column(7, 7, 10)
        worksheet.set_column(8, 8, 10)
        worksheet.set_column(9, 9, 10)
        worksheet.set_column(10, 10, 15)
        worksheet.set_column(11, 11, 15)
        worksheet.set_column(12, 12, 15)

        tit = workbook.add_format({'border': 2,
                                   'font_name': 'Arial',
                                   'font_size': '12'})
        tot = workbook.add_format({'border': 2,
                                   'bold': True,
                                   'font_name': 'Arial',
                                   'font_size': '10'})
        border = workbook.add_format({'border': 2,
                                      'font_name': 'Arial',
                                      'font_size': '10'})
        format1 = workbook.add_format({'border': 2,
                                       'bold': True,
                                       'font_name': 'Arial',
                                       'font_size': '10'})
        format1.set_bg_color('gray')
        row = 0
        row += 1
        row += 1
        worksheet.write(row, 1, 'Fleet Listing', tit)
        row = 1
        row += 3
        worksheet.write(row, 0, 'NO', format1)
        worksheet.write(row, 1, 'Vehicle ID', format1)
        worksheet.write(row, 2, 'VIN NO.', format1)
        worksheet.write(row, 3, 'ENGINE NO', format1)
        worksheet.write(row, 4, 'METER', format1)
        worksheet.write(row, 5, 'MAKE', format1)
        worksheet.write(row, 6, 'MODEL', format1)
        worksheet.write(row, 7, 'COLOR', format1)
        worksheet.write(row, 8, 'TYPE', format1)
        worksheet.write(row, 9, 'DRIVER NAME.', format1)
        worksheet.write(row, 10, 'DRIVER CONTACT', format1)
        line_row = row + 1
        line_col = 0
        counter = 1
        for obj in fleet_listing:
            worksheet.write(line_row, line_col, counter, border)
            line_col += 1
            worksheet.write(line_row, line_col, obj.name or '', border)
            line_col += 1
            worksheet.write(line_row, line_col, obj.vin_sn or '', border)
            line_col += 1
            worksheet.write(line_row, line_col, obj.engine_no or '', border)
            line_col += 1
            worksheet.write(line_row, line_col, obj.odometer or '', border)
            line_col += 1
            worksheet.write(line_row, line_col, obj.f_brand_id and
                            obj.f_brand_id.name or '', border)
            line_col += 1
            worksheet.write(line_row, line_col, obj.model_id and
                            obj.model_id.name or '', border)
            line_col += 1
            worksheet.write(line_row, line_col, obj.vehical_color_id and
                            obj.vehical_color_id.name or '', border)
            line_col += 1
            worksheet.write(line_row, line_col, obj.vechical_type_id and
                            obj.vechical_type_id.name or '', border)
            line_col += 1
            worksheet.write(line_row, line_col, obj.driver_id and
                            obj.driver_id.name or '', border)
            line_col += 1
            worksheet.write(line_row, line_col, obj.driver_contact_no or '',
                            border)
            line_col = 0
            line_row += 1
            counter += 1
        worksheet.write(line_row, line_col, '********', border)
        row += 5

FleetListing('report.fleet.summary.xls', 'fleet.vehicle')
