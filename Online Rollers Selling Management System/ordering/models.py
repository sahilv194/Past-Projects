from django.db import models

class Admin(models.Model):
    admin_id = models.IntegerField(primary_key=True)
    admin_name = models.CharField(max_length=40)
    email_id = models.CharField(db_column='Email_id', max_length=40)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'admin'


class Area(models.Model):
    pincode = models.IntegerField(db_column='Pincode', primary_key=True)  # Field name made lowercase.
    area_name = models.CharField(db_column='Area_Name', max_length=50)  # Field name made lowercase.
    city = models.ForeignKey('City', models.DO_NOTHING, db_column='City_id')  # Field name made lowercase.

    def __str__(self):
        return self.area_name

    class Meta:
        managed = False
        db_table = 'area'


class BillingDetailTable(models.Model):
    bill_d_id = models.AutoField(db_column='Bill D_ID', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    bill = models.ForeignKey('BillingTable', models.DO_NOTHING, db_column='BILL_ID')  # Field name made lowercase.
    p = models.ForeignKey('ProductTable', models.DO_NOTHING, db_column='P_id')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=60)  # Field name made lowercase.
    quantity = models.CharField(db_column='Quantiy', max_length=10)  # Field name made lowercase.
    rate = models.CharField(db_column='Rate', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'billing detail table'


class BillingTable(models.Model):
    bill_id = models.AutoField(db_column='BILL_id', primary_key=True)  # Field name made lowercase.
    so = models.ForeignKey('SalesOrderTable', models.DO_NOTHING, db_column='SO_id')  # Field name made lowercase.
    bill_date = models.DateField(db_column='Bill_Date')  # Field name made lowercase.
    total = models.CharField(db_column='Total', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'billing table'


class City(models.Model):
    city_id = models.AutoField(db_column='City_Id', primary_key=True)  # Field name made lowercase.
    city_name = models.CharField(db_column='City_Name', max_length=50)  # Field name made lowercase.
    state = models.ForeignKey('State', models.DO_NOTHING, db_column='State_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'city'


class Customer(models.Model):
    cust_id = models.AutoField(db_column='Cust_id', primary_key=True)  # Field name made lowercase.
    customer_name = models.CharField(db_column='Customer_Name', max_length=40)  # Field name made lowercase.
    customer_address = models.CharField(db_column='Customer_Address', max_length=80)  # Field name made lowercase.
    contact_no_field = models.CharField(db_column='Contact No.', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    password = models.CharField(db_column='Password', max_length=20)  # Field name made lowercase.
    email_id = models.CharField(db_column='Email_Id', max_length=40)  # Field name made lowercase.
    pincode = models.ForeignKey(Area, models.DO_NOTHING, db_column='Pincode')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'customer'


class Employee(models.Model):
    e_id = models.AutoField(primary_key=True)
    e_name = models.CharField(max_length=20)
    j_date = models.DateField()
    e_email_id = models.CharField(db_column='e_Email id', max_length=40)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    e_contact = models.CharField(max_length=20)
    e_address = models.CharField(db_column='e_Address', max_length=100)  # Field name made lowercase.
    e_city = models.CharField(db_column='e_City', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'employee'


class Material(models.Model):
    m_id = models.AutoField(db_column='M_id', primary_key=True)  # Field name made lowercase.
    m_name = models.CharField(db_column='M_name', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'material'


class MaterialStockTable(models.Model):
    stock_id = models.AutoField(db_column='Stock_id', primary_key=True)  # Field name made lowercase.
    p = models.ForeignKey('ProductTable', models.DO_NOTHING, db_column='P_id')  # Field name made lowercase.
    transaction_type = models.CharField(db_column='Transaction_type', max_length=10)  # Field name made lowercase.
    t_datetime = models.DateTimeField(db_column='T_datetime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'material stock table'

class PaynmentTable(models.Model):
    py_id = models.AutoField(db_column='Py_id', primary_key=True)  # Field name made lowercase.
    po_id = models.IntegerField(db_column='PO_id')  # Field name made lowercase.
    py_date = models.DateField(db_column='Py_date')  # Field name made lowercase.
    amount = models.CharField(db_column='Amount', max_length=10)  # Field name made lowercase.
    p_mode = models.CharField(db_column='P_Mode', max_length=10)  # Field name made lowercase.
    transaction_no = models.CharField(db_column='Transaction no', max_length=15)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'paynment table'


class Product(models.Model):
    p_id = models.IntegerField(primary_key=True)
    p_name = models.CharField(max_length=30)
    pt_id = models.IntegerField()
    m_id = models.IntegerField()
    gage = models.IntegerField(db_column='Gage')  # Field name made lowercase.
    p_image = models.TextField()
    p_description = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'product'


class ProductTable(models.Model):
    p_id = models.AutoField(db_column='P_id', primary_key=True)  # Field name made lowercase.
    p_name = models.CharField(db_column='P_name', max_length=30)  # Field name made lowercase.
    p_type = models.CharField(db_column='P_type', max_length=30)  # Field name made lowercase.
    gauge = models.CharField(db_column='Gauge', max_length=5, blank=True, null=True)  # Field name made lowercase.
    gauge_u = models.ForeignKey('UnitTable', models.DO_NOTHING, db_column='Gauge U_id')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    m = models.ForeignKey(Material, models.DO_NOTHING, db_column='M_id')  # Field name made lowercase.
    rate_per_mm = models.CharField(db_column='Rate per mm', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    p_image = models.CharField(db_column='P_Image', max_length=100, blank=True, null=True)  # Field name made lowercase.
    p_description = models.CharField(db_column='P_Description', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'product table'

class ProductType(models.Model):
    pt_id = models.AutoField(primary_key=True)
    pt_name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'product type'


class PurchaseOrderDetailTable(models.Model):
    pd_id = models.AutoField(db_column='PD_id', primary_key=True)  # Field name made lowercase.
    po_id = models.IntegerField(db_column='PO_id')  # Field name made lowercase.
    p_id = models.IntegerField(db_column='P_id')  # Field name made lowercase.
    length = models.CharField(db_column='Length', max_length=10)  # Field name made lowercase.
    lengthu_id = models.IntegerField(db_column='Lengthu_id')  # Field name made lowercase.
    quantity = models.CharField(db_column='Quantity', max_length=10)  # Field name made lowercase.
    rate = models.CharField(db_column='Rate', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'purchase order detail table'


class PurchaseOrderTable(models.Model):
    po_id = models.AutoField(db_column='PO_id', primary_key=True)  # Field name made lowercase.
    supplier_id = models.IntegerField(db_column='Supplier_id')  # Field name made lowercase.
    po_date = models.DateField(db_column='PO_Date')  # Field name made lowercase.
    po_total = models.CharField(db_column='PO_Total', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'purchase order table'


class ReadyProductTable(models.Model):
    pstock_id = models.AutoField(db_column='Pstock_id', primary_key=True)  # Field name made lowercase.
    p_id = models.IntegerField(db_column='P_id')  # Field name made lowercase.
    sd_id = models.IntegerField(db_column='SD_id')  # Field name made lowercase.
    quantity = models.CharField(db_column='Quantity', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ready product table'


class ReceiptTable(models.Model):
    r_id = models.AutoField(db_column='R_id', primary_key=True)  # Field name made lowercase.
    so_id = models.IntegerField(db_column='SO_id')  # Field name made lowercase.
    r_date = models.DateField(db_column='R_date')  # Field name made lowercase.
    amount = models.CharField(db_column='Amount', max_length=10)  # Field name made lowercase.
    mode = models.CharField(db_column='Mode', max_length=30)  # Field name made lowercase.
    transaction_no = models.CharField(db_column='Transaction no', max_length=15)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'receipt table'


class SalesOrderDetailTable(models.Model):
    sd_id = models.AutoField(db_column='SD_id', primary_key=True)  # Field name made lowercase.
    so = models.ForeignKey('SalesOrderTable', models.DO_NOTHING, db_column='SO_id')  # Field name made lowercase.
    p = models.ForeignKey(ProductTable, models.DO_NOTHING, db_column='P_id')  # Field name made lowercase.
    length = models.FloatField(db_column='Length')  # Field name made lowercase.
    diameter = models.FloatField(db_column='Diameter')  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity')  # Field name made lowercase.
    rate = models.IntegerField(db_column='Rate')  # Field name made lowercase.
    image = models.CharField(db_column='Image', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sales order detail table'

class SalesOrderTable(models.Model):
    so_id = models.AutoField(db_column='SO_id', primary_key=True)  # Field name made lowercase.
    cust = models.ForeignKey(Customer, models.DO_NOTHING, db_column='Cust_id')  # Field name made lowercase.
    sales_date = models.DateField(db_column='Sales_Date')  # Field name made lowercase.
    total = models.CharField(db_column='Total', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sales order table'


class State(models.Model):
    state_id = models.AutoField(db_column='State_id', primary_key=True)  # Field name made lowercase.
    state_name = models.CharField(db_column='State_name', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'state'


class Supplier(models.Model):
    supplier_id = models.AutoField(db_column='Supplier_id', primary_key=True)  # Field name made lowercase.
    supplier_name = models.CharField(db_column='Supplier_name', max_length=50)  # Field name made lowercase.
    supplier_address = models.CharField(db_column='Supplier_Address', max_length=80)  # Field name made lowercase.
    supplier_contact = models.CharField(db_column='Supplier_Contact', max_length=20)  # Field name made lowercase.
    supplier_email_id = models.CharField(db_column='Supplier_Email Id', max_length=40)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'supplier'


class UnitTable(models.Model):
    unit_id = models.AutoField(db_column='Unit_id', primary_key=True)  # Field name made lowercase.
    unit_name = models.CharField(db_column='Unit_name', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'unit table'

        
class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    cust = models.ForeignKey('Customer', models.DO_NOTHING)
    p = models.ForeignKey('ProductTable', models.DO_NOTHING)
    length = models.FloatField()
    diameter = models.FloatField()
    quantity = models.IntegerField()
    rate = models.FloatField()
    total = models.FloatField()
    image = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cart'