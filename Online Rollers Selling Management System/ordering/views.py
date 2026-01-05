from django.shortcuts import render,redirect
from .models import State,UnitTable,Area,City,Admin,Employee,Customer,Supplier,ProductType,Material,PurchaseOrderTable,SalesOrderTable,BillingTable,ProductTable,MaterialStockTable,PaynmentTable,ReceiptTable,ReadyProductTable,SalesOrderDetailTable,PurchaseOrderDetailTable,BillingDetailTable,Cart
from django.core.files.storage import FileSystemStorage
from datetime import datetime
# Create your views here.
def employeelist(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    amp=Employee.objects.all()
    return render(request,"employeelist.html",{'employees':amp})
def employeereport(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    amp=Employee.objects.all()
    return render(request,"employeereport.html",{'employees':amp})

def employeeadd(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    return render(request,"employeeadd.html")
def employeesave(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    if(request.method=="POST"):
        eid=request.POST.get('eid')
        ename=request.POST.get('ename')
        jdate=request.POST.get('jdate')
        eemail=request.POST.get('eemail')
        econt=request.POST.get('econt')
        eadd=request.POST.get('eadd')
        ecity=request.POST.get('ecity')
        employee=Employee(e_id=eid,e_name=ename,j_date=jdate,e_email_id=eemail,e_contact=econt,e_address=eadd,e_city=ecity)
        employee.save()
        return redirect("/employeelist/")
def employeedel(request,id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    employee=Employee.objects.get(e_id=id)
    employee.delete()
    return redirect("/employeelist/")
def employeeupdate(request,id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    eid=request.POST.get('eid')
    ename=request.POST.get('ename')
    jdate=request.POST.get('jdate')
    eemail=request.POST.get('eemail')
    econt=request.POST.get('econt')
    eadd=request.POST.get('eadd')
    ecity=request.POST.get('ecity')
    employee=Employee(e_id=eid,e_name=ename,j_date=jdate,e_email_id=eemail,e_contact=econt,e_address=eadd,e_city=ecity)
    employee.save()
    return redirect("/employeelist/")
def employeeedit(request,id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    employee=Employee.objects.get(e_id=id,)
    return render(request,"employeeedit.html",{'employee':employee})



def adminlist(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    adm=Admin.objects.all()
    return render(request,"adminlist.html",{'admins':adm})
def adminadd(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    return render(request,"adminadd.html")
def adminsave(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    if(request.method=="POST"):
        aid=request.POST.get('aid')
        aname=request.POST.get('aname')
        eid=request.POST.get('eid')
        pname=request.POST.get('pname')
        admin=Admin(admin_id=aid,admin_name=aname,email_id=eid,password=pname)
        admin.save()
        return redirect("/adminlist/")
def admindel(request,id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    admin=Admin.objects.get(admin_id=id)
    admin.delete()
    return redirect("/adminlist/")
def adminupdate(request,id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    aid=request.POST.get('aid')
    aname=request.POST.get('aname')
    eid=request.POST.get('eid')
    pname=request.POST.get('pname')
    admin=Admin(admin_id=aid,admin_name=aname,email_id=eid,password=pname)
    admin.save()
    return redirect("/adminlist/")
def adminedit(request,id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    admin=Admin.objects.get(admin_id=id,)
    return render(request,"adminedit.html",{'admin':admin})



def show(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    sts=State.objects.all()
    return render(request,"list.html",{'states':sts})
def listreport(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    sts=State.objects.all()
    return render(request,"listreport.html",{'states':sts})

def stateadd(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    return render(request,"listadd.html")
def statesave(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    if(request.method=="POST"):
        sname=request.POST.get('sname')
        state=State(state_name=sname)
        state.save()
        return redirect("/slist/")
def statedel(request,id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    state=State.objects.get(state_id=id)
    state.delete()
    return redirect("/slist/")
def stateupdate(request,id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    sid=request.POST.get('sid')
    sname=request.POST.get('sname')
    state=State(state_id=sid,state_name=sname)
    state.save()
    return redirect("/slist/")
def stateedit(request,id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    state=State.objects.get(state_id=id)
    return render(request,"listedit.html",{'state':state})



def unitlist(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    uts=UnitTable.objects.all()
    return render(request,"unit.html",{'units':uts})
def unitadd(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    return render(request,"unitadd.html")
def unitsave(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    if(request.method=="POST"):
        uid=request.POST.get('uid')
        uname=request.POST.get('uname')
        unit=UnitTable(unit_id=uid,unit_name=uname)
        unit.save()
        return redirect("/ulist/")
def unitdel(request,id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    unit=UnitTable.objects.get(unit_id=id)
    unit.delete()
    return redirect("/ulist/")
def unitupdate(request,id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    uid=request.POST.get('uid')
    un=request.POST.get('uname')
    unit=UnitTable(unit_id=uid,unit_name=un)
    unit.save()
    return redirect("/ulist/")
def unitedit(request,id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    unit=UnitTable.objects.get(unit_id=id)
    return render(request,"unitedit.html",{'unit':unit})



def arealist(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    are=Area.objects.all()
    return render(request,"arealist.html",{'areas':are})
def areaadd(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    cty=City.objects.all()
    return render(request,"areaadd.html",{'citys':cty})
def areasave(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    if(request.method=="POST"):
        pin=request.POST.get('pin')
        aname=request.POST.get('aname')
        cname=request.POST.get('cname')
        area=Area(pincode=pin,area_name=aname,city_id=cname)
        area.save()
        return redirect("/alist/")
def areatdel(request,id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    area=Area.objects.get(pincode=id)
    area.delete()
    return redirect("/alist/")
def areaupdate(request,id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    pin=request.POST.get('pin')
    aname=request.POST.get('aname')
    cname=request.POST.get('cname')
    area=Area(pincode=pin,area_name=aname,city_id=cname)
    area.save()
    return redirect("/alist/")
def areaedit(request,id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    cty=City.objects.all()
    area=Area.objects.get(pincode=id)
    return render(request,"areaedit.html",{'citys':cty,'area':area})



def citylist(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    cty=City.objects.all()
    return render(request,"citylist.html",{'citys':cty})
def cityadd(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    sts=State.objects.all()
    return render(request,"cityadd.html",{'states':sts})
def citysave(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    if(request.method=="POST"):
        cid=request.POST.get('cid')
        cname=request.POST.get('cname')
        sname=request.POST.get('sname')
        city=City(city_id=cid,city_name=cname,state_id=sname)
        city.save()
        return redirect("/citylist/")
def citytdel(request,id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    city=City.objects.get(city_id=id)
    city.delete()
    return redirect("/citylist/")
def cityupdate(request,id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    cid=request.POST.get('cid')
    cname=request.POST.get('cname')
    sname=request.POST.get('sname')
    city=City(city_id=cid,city_name=cname,state_id=sname)
    city.save()
    return redirect("/citylist/")
def cityedit(request,id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    sts=State.objects.all()
    city=City.objects.get(city_id=id)
    return render(request,"cityedit.html",{'states':sts,'city':city})



def customerlist(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    cus=Customer.objects.all()
    return render(request,"customerlist.html",{'customers':cus})
def customerreport(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    cus=Customer.objects.all()
    return render(request,"customerreport.html",{'customers':cus})

def customeradd(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    areas=Area.objects.all()
    return render(request,"customeradd.html",{'areas':areas})
def customersave(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    if(request.method=="POST"):
        cid=request.POST.get('cid')
        cname=request.POST.get('cname')
        caddress=request.POST.get('caddress')
        ccontact=request.POST.get('ccontact')
        cpassword=request.POST.get('cpassword')
        cemailid=request.POST.get('cemailid')
        cpincode=request.POST.get('cpincode')
        area=Area.objects.get(pincode=cpincode)
        customer=Customer(cust_id=cid,customer_name=cname,customer_address=caddress,contact_no_field=ccontact,password=cpassword,email_id=cemailid,pincode=area)
        customer.save()
        return redirect("/customerlist/")  
def customerdel(request,id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    customer=Customer.objects.get(cust_id=id)
    customer.delete()
    return redirect("/customerlist/")
def customerupdate(request,id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    cid=request.POST.get('cid')
    cname=request.POST.get('cname')
    caddress=request.POST.get('caddress')
    ccontact=request.POST.get('ccontact')
    cpassword=request.POST.get('cpassword')
    cemailid=request.POST.get('cemailid')
    cpincode=request.POST.get('cpincode')
    area=Area.objects.get(pincode=cpincode)
    customer=Customer(cust_id=cid,customer_name=cname,customer_address=caddress,contact_no_field=ccontact,password=cpassword,email_id=cemailid,pincode=area)
    customer.save()
    return redirect("/customerlist/")
def customeredit(request,id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    areas=Area.objects.all()
    customer=Customer.objects.get(cust_id=id)
    return render(request,"customeredit.html",{'areas':areas,'customer':customer})



def supplierlist(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    sup=Supplier.objects.all()
    return render(request,"supplierlist.html",{'suppliers':sup})
def supplierreport(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    sup=Supplier.objects.all()
    return render(request,"supplierreport.html",{'suppliers':sup})

def supplieradd(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    return render(request,"supplieradd.html")
def suppliersave(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    if(request.method=="POST"):
        sid=request.POST.get('sid')
        sname=request.POST.get('sname')
        saddress=request.POST.get('saddress')
        scontact=request.POST.get('scontact')
        semailid=request.POST.get('semailid')
        supplier=Supplier(supplier_id=sid,supplier_name=sname,supplier_address=saddress,supplier_contact=scontact,supplier_email_id=semailid)
        supplier.save()
        return redirect("/supplierlist/")
def supplierdel(request,id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    supplier=Supplier.objects.get(supplier_id=id)
    supplier.delete()
    return redirect("/supplierlist/")
def supplierupdate(request,id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    sid=request.POST.get('sid')
    sname=request.POST.get('sname')
    saddress=request.POST.get('saddress')
    scontact=request.POST.get('scontact')
    semailid=request.POST.get('semailid')
    supplier=Supplier(supplier_id=sid,supplier_name=sname,supplier_address=saddress,supplier_contact=scontact,supplier_email_id=semailid)
    supplier.save()
    return redirect("/supplierlist/")
def supplieredit(request,id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    supplier=Supplier.objects.get(supplier_id=id)
    return render(request,"supplieredit.html",{'supplier':supplier})


    
def producttypelist(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    prt=ProductType.objects.all()
    return render(request,"producttypelist.html",{'producttypes':prt})
def producttypeadd(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    return render(request,"producttypeadd.html")
def producttypesave(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    if(request.method=="POST"):
        ptid=request.POST.get('ptid')
        ptname=request.POST.get('ptname')
        producttype=ProductType(pt_id=ptid,pt_name=ptname)
        producttype.save()
        return redirect("/producttypelist/")
def producttypedel(request,id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    producttype=ProductType.objects.get(pt_id=id)
    producttype.delete()
    return redirect("/producttypelist/")
def producttypeupdate(request,id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    ptid=request.POST.get('ptid')
    ptname=request.POST.get('ptname')
    producttype=ProductType(pt_id=ptid,pt_name=ptname)
    producttype.save()
    return redirect("/producttypelist/")
def producttypeedit(request,id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    producttype=ProductType.objects.get(pt_id=id)
    return render(request,"producttypeedit.html",{'producttype':producttype})



def materiallist(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    mtr=Material.objects.all()
    return render(request,"materiallist.html",{'materials':mtr})
def materialadd(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    return render(request,"materialadd.html")
def materialsave(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    if(request.method=="POST"):
        mid=request.POST.get('mid')
        mname=request.POST.get('mname')
        material=Material(m_id=mid,m_name=mname)
        material.save()
        return redirect("/materiallist/")
def materialdel(request,id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    material=Material.objects.get(m_id=id)
    material.delete()
    return redirect("/materiallist/")
def materialupdate(request,id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    mid=request.POST.get('mid')
    mname=request.POST.get('mname')
    material=Material(m_id=mid,m_name=mname)
    material.save()
    return redirect("/materiallist/")
def materialedit(request,id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    material=Material.objects.get(m_id=id)
    return render(request,"materialedit.html",{'material':material})



def purchaseorderlist(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    pod=PurchaseOrderDetailTable.objects.all()
    pro=PurchaseOrderTable.objects.all()
    return render(request,"purchaseorderlist.html",{'purchaseorders':pro,'purchaseorderdetailtables':pod}) 
      
def purchaseorderlistd(request,id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    pod=PurchaseOrderDetailTable.objects.filter(po_id=id)
    pro=PurchaseOrderTable.objects.all()
    return render(request,"purchaseorderlist.html",{'purchaseorders':pro,'purchaseorderdetailtables':pod})   

def purchaseorderadd(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    suppliers=Supplier.objects.all()
    return render(request,"purchaseorderadd.html",{'suppliers':suppliers})
def purchaseordersave(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    if(request.method=="POST"):
        poid=request.POST.get('poid')
        sid=request.POST.get('sid')
        podate=request.POST.get('podate')
        pototal=request.POST.get('pototal')
        purchaseorder=PurchaseOrderTable(po_id=poid,supplier_id=sid,po_date=podate,po_total=pototal)
        purchaseorder.save()
        return redirect("/purchaseorderlist/")
def purchaseorderdel(request,id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    purchaseorder=PurchaseOrderTable.objects.get(po_id=id)
    purchaseorder.delete()
    return redirect("/purchaseorderlist/")
def purchaseorderupdate(request,id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    poid=request.POST.get('poid')
    sid=request.POST.get('sid')
    podate=request.POST.get('podate')
    pototal=request.POST.get('pototal')
    purchaseorder=PurchaseOrderTable(po_id=poid,supplier_id=sid,po_date=podate,po_total=pototal)
    purchaseorder.save()
    return redirect("/purchaseorderlist/")
def purchaseorderedit(request,id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    suppliers=Supplier.objects.all()
    purchaseorder=PurchaseOrderTable.objects.get(po_id=id)
    return render(request,"purchaseorderedit.html",{'suppliers':suppliers,'purchaseorder':purchaseorder})



def salesorderlist(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    sod=SalesOrderDetailTable.objects.all()
    slo=SalesOrderTable.objects.all()
    return render(request,"salesorderlist.html",{'salesorders':slo,'salesorderdetailtables':sod})

def salesorderlistd(request,id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    sod=SalesOrderDetailTable.objects.filter(so_id=id)
    slo=SalesOrderTable.objects.all()
    return render(request,"salesorderlist.html",{'salesorders':slo,'salesorderdetailtables':sod})

def salesorderadd(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    customers=Customer.objects.all()
    return render(request,"salesorderadd.html",{'customers':customers})
def salesordersave(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    if(request.method=="POST"):
        soid=request.POST.get('soid')
        cid=request.POST.get('cid')
        sodate=request.POST.get('sodate')
        sototal=request.POST.get('sototal')
        salesorder=SalesOrderTable(so_id=soid,cust_id=cid,sales_date=sodate,total=sototal)
        salesorder.save()
        return redirect("/salesorderlist/")
def salesorderdel(request,id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    salesorder=SalesOrderTable.objects.get(so_id=id)
    salesorder.delete()
    return redirect("/salesorderlist/")
def salesorderupdate(request,id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    soid=request.POST.get('soid')
    cid=request.POST.get('cid')
    sodate=request.POST.get('sodate')
    sototal=request.POST.get('sototal')
    salesorder=SalesOrderTable(so_id=soid,cust_id=cid,sales_date=sodate,total=sototal)
    salesorder.save()
    return redirect("/salesorderlist/")
def salesorderedit(request,id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    customers=Customer.objects.all()
    salesorder=SalesOrderTable.objects.get(so_id=id)
    return render(request,"salesorderedit.html",{'customers':customers,'salesorder':salesorder})


def billinglist(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    bill=BillingTable.objects.all()
    return render(request,"billinglist.html",{'billingtables':bill})
def billingadd(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    slo=SalesOrderTable.objects.all()
    return render(request,"billingadd.html",{'salesordertables':slo})
def billingsave(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    if(request.method=="POST"):
        bid=request.POST.get('bid')
        soid=request.POST.get('soid')
        bdate=request.POST.get('bdate')
        btotal=request.POST.get('btotal')
        sot=SalesOrderTable.objects.get(so_id=soid)
        bo=BillingTable(bill_id=bid,so_id=soid,bill_date=bdate,total=btotal)
        bo.save()
        return redirect("/billinglist/")
def billingdel(request,id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    billing=BillingTable.objects.get(bill_id=id)
    billing.delete()
    return redirect("/billinglist/")
def billingupdate(request,id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    bid=request.POST.get('bid')
    soid=request.POST.get('soid')
    bdate=request.POST.get('bdate')
    btotal=request.POST.get('btotal')
    sot=SalesOrderTable.objects.get(so_id=soid)
    bo=BillingTable(bill_id=bid,so_id=soid,bill_date=bdate,total=btotal)
    bo.save()
    return redirect("/billinglist/")
def billingedit(request,id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    slo=SalesOrderTable.objects.all()
    billing=BillingTable.objects.get(bill_id=id)
    return render(request,"billingedit.html",{'salesordertables':slo,'bill':billing})



def productlist(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    prt=ProductTable.objects.all()
    return render(request,"productlist.html",{'producttables':prt})
def productadd(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    unit=UnitTable.objects.all()
    material=Material.objects.all()
    return render(request,"productadd.html",{'unittables':unit,'material':material})
def productsave(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    if(request.method=="POST"):
        pname=request.POST.get('pname')
        ptype=request.POST.get('ptype')
        gauge=request.POST.get('gauge')
        gunitid=request.POST.get('gunitid')
        m_id=request.POST.get('mid')
        rpm=request.POST.get('rpm')
        pimage=request.FILES['pimage']
        fss=FileSystemStorage()
        file=fss.save(pimage.name,pimage)
        fileurl=fss.url(file)
        pdescription=request.POST.get('pdescription')
        product=ProductTable(p_name=pname,p_type=ptype,gauge=gauge,gauge_u_id=gunitid,m_id=m_id,rate_per_mm=rpm,p_image=fileurl,p_description=pdescription)
        product.save()
        return redirect("/productlist/")
def productdel(request,id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    product=ProductTable.objects.get(p_id=id)
    product.delete()
    return redirect("/productlist/")
def productupdate(request,id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    pid=request.POST.get('pid')
    pname=request.POST.get('pname')
    ptype=request.POST.get('ptype')
    gauge=request.POST.get('gauge')
    gunitid=request.POST.get('gunitid')
    m_id=request.POST.get('mid')
    rpm=request.POST.get('rpm')
    pimage=request.FILES['pimage']
    fss=FileSystemStorage()
    file=fss.save(pimage.name,pimage)
    fileurl=fss.url(file)
    pdescription=request.POST.get('pdescription')
    product=ProductTable(p_id=pid,p_name=pname,p_type=ptype,gauge=gauge,gauge_u_id=gunitid,m_id=m_id,rate_per_mm=rpm,p_image=fileurl,p_description=pdescription)
    product.save()
    return redirect("/productlist/")
def productedit(request,id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    unit=UnitTable.objects.all()
    material=Material.objects.all()
    product=ProductTable.objects.get(p_id=id)
    return render(request,"productedit.html",{'unittables':unit,'material':material,'product':product})



def materialstocklist(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    mts=MaterialStockTable.objects.all()
    return render(request,"materialstocklist.html",{'materialstocktables':mts})
def materialstockreport(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    mts=MaterialStockTable.objects.all()
    return render(request,"materialstockreport.html",{'materialstocktables':mts})

def materialstockadd(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    producttable=ProductTable.objects.all()
    return render(request,"materialstockadd.html",{'producttables':producttable})
def materialstocksave(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    if(request.method=="POST"):
        msid=request.POST.get('msid')
        pid=request.POST.get('pid')
        ttype=request.POST.get('ttype')
        tdatetime=request.POST.get('tdatetime')
        materialstock=MaterialStockTable(stock_id=msid,p=pid,transaction_type=ttype,t_datetime=tdatetime)
        materialstock.save()
        return redirect("/materialstocklist/")
def materialstockdel(request,id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    materialstock=MaterialStockTable.objects.get(stock_id=id)
    materialstock.delete()
    return redirect("/materialstocklist/")
def materialstockupdate(request,id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    msid=request.POST.get('msid')
    pid=request.POST.get('pid')
    ttype=request.POST.get('ttype')
    tdatetime=request.POST.get('tdatetime')
    materialstock=MaterialStockTable(stock_id=msid,p=pid,transaction_type=ttype,t_datetime=tdatetime)
    materialstock.save()
    return redirect("/materialstocklist/")
def materialstockedit(request,id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    producttable=ProductTable.objects.all()
    materialstock=MaterialStockTable.objects.get(stock_id=id)
    return render(request,"materialstockedit.html",{'producttables':producttable,'materialstock':materialstock})



def paymentlist(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    pyt=PaynmentTable.objects.all()
    return render(request,"paymentlist.html",{'paynmenttables':pyt})
def paymentadd(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    purchaseorder=PurchaseOrderTable.objects.all()
    return render(request,"paymentadd.html",{'purchaseordertables':purchaseorder})
def paymentsave(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    if(request.method=="POST"):
        pyid=request.POST.get('pyid')
        poid=request.POST.get('poid')
        pydate=request.POST.get('pydate')
        amount=request.POST.get('amount')
        pymode=request.POST.get('pymode')
        tno=request.POST.get('tno')
        payment=PaynmentTable(py_id=pyid,po_id=poid,py_date=pydate,amount=amount,p_mode=pymode,transaction_no=tno)
        payment.save()
        return redirect("/paymentlist/")
def paymentdel(request,id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    payment=PaynmentTable.objects.get(py_id=id)
    payment.delete()
    return redirect("/paymentlist/")
def paymentupdate(request,id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    pyid=request.POST.get('pyid')
    poid=request.POST.get('poid')
    pydate=request.POST.get('pydate')
    amount=request.POST.get('amount')
    pymode=request.POST.get('pymode')
    tno=request.POST.get('tno')
    payment=PaynmentTable(py_id=pyid,po_id=poid,py_date=pydate,amount=amount,p_mode=pymode,transaction_no=tno)
    payment.save()
    return redirect("/paymentlist/")
def paymentedit(request,id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    purchaseorder=PurchaseOrderTable.objects.all()
    payment=PaynmentTable.objects.get(py_id=id)
    return render(request,"paymentedit.html",{'purchaseordertables':purchaseorder,'payment':payment})



def receiptlist(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    rcp=ReceiptTable.objects.all()
    return render(request,"receiptlist.html",{'receipttables':rcp})
def receiptadd(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    salesorder=SalesOrderTable.objects.all()
    return render(request,"receiptadd.html",{'salesordertables':salesorder})
def receiptsave(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    if(request.method=="POST"):
        rid=request.POST.get('rid')
        soid=request.POST.get('soid')
        rdate=request.POST.get('rdate')
        amount=request.POST.get('amount')
        mode=request.POST.get('mode')
        tno=request.POST.get('tno')
        receipt=ReceiptTable(r_id=rid,so_id=soid,r_date=rdate,amount=amount,mode=mode,transaction_no=tno)
        receipt.save()
        return redirect("/receiptlist/")
def receiptdel(request,id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    receipt=ReceiptTable.objects.get(r_id=id)
    receipt.delete()
    return redirect("/receiptlist/")
def receiptupdate(request,id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    rid=request.POST.get('rid')
    soid=request.POST.get('soid')
    rdate=request.POST.get('rdate')
    amount=request.POST.get('amount')
    mode=request.POST.get('mode')
    tno=request.POST.get('tno')
    receipt=ReceiptTable(r_id=rid,so_id=soid,r_date=rdate,amount=amount,mode=mode,transaction_no=tno)
    receipt.save()
    return redirect("/receiptlist/")
def receiptedit(request,id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    salesorder=SalesOrderTable.objects.all()
    receipt=ReceiptTable.objects.get(r_id=id)
    return render(request,"receiptedit.html",{'salesordertables':salesorder,'receipt':receipt})



def readyproductlist(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    rpt=ReadyProductTable.objects.all()
    return render(request,"readyproductlist.html",{'readyproducttables':rpt})
def readyproductadd(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    product=ProductTable.objects.all()
    salesorderdetail=SalesOrderDetailTable.objects.all()
    return render(request,"readyproductadd.html",{'producttables':product,'salesorderdetailtable':salesorderdetail})
def readyproductsave(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    if(request.method=="POST"):
        rpid=request.POST.get('rpid')
        pid=request.POST.get('pid')
        sdid=request.POST.get('sdid')
        quantity=request.POST.get('quantity')
        readyproduct=ReadyProductTable(pstock_id=rpid,p_id=pid,sd_id=sdid,quantity=quantity)
        readyproduct.save()
        return redirect("/readyproductlist/")
def readyproductdel(request,id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    readyproduct=ReadyProductTable.objects.get(pstock_id=id)
    readyproduct.delete()
    return redirect("/readyproductlist/")
def readyproductupdate(request,id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    rpid=request.POST.get('rpid')
    pid=request.POST.get('pid')
    sdid=request.POST.get('sdid')
    quantity=request.POST.get('quantity')
    readyproduct=ReadyProductTable(pstock_id=rpid,p_id=pid,sd_id=sdid,quantity=quantity)
    readyproduct.save()
    return redirect("/readyproductlist/")
def readyproductedit(request,id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    product=ProductTable.objects.all()
    salesorderdetail=SalesOrderDetailTable.objects.all()
    readyproduct=ReadyProductTable.objects.get(pstock_id=id)
    return render(request,"readyproductedit.html",{'producttables':product,'salesorderdetailtable':salesorderdetail,'readyproduct':readyproduct})



def purchaseorderdetaillist(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    pod=PurchaseOrderDetailTable.objects.all()
    return render(request,"purchaseorderdetaillist.html",{'purchaseorderdetailtables':pod})
def purchaseorderdetailadd(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    purchaseorder=PurchaseOrderTable.objects.all()
    product=ProductTable.objects.all()
    unit=UnitTable.objects.all()
    return render(request,"purchaseorderdetailadd.html",{'purchaseordertables':purchaseorder,'producttable':product,'unittable':unit})
def purchaseorderdetailsave(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    if(request.method=="POST"):
        pdid=request.POST.get('pdid')
        poid=request.POST.get('poid')
        pid=request.POST.get('pid')
        length=request.POST.get('length')
        lengthuid=request.POST.get('lengthuid')
        quantity=request.POST.get('quantity')
        rate=request.POST.get('rate')
        purchaseorderdetail=PurchaseOrderDetailTable(pd_id=pdid,po_id=poid,p_id=pid,length=length,lengthu_id=lengthuid,quantity=quantity,rate=rate)
        purchaseorderdetail.save()
        return redirect("/purchaseorderdetaillist/")
def purchaseorderdetaildel(request,id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    purchaseorderdetail=PurchaseOrderDetailTable.objects.get(pd_id=id)
    purchaseorderdetail.delete()
    return redirect("/purchaseorderdetaillist/")
def purchaseorderdetailupdate(request,id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    pdid=request.POST.get('pdid')
    poid=request.POST.get('poid')
    pid=request.POST.get('pid')
    length=request.POST.get('length')
    lengthuid=request.POST.get('lengthuid')
    quantity=request.POST.get('quantity')
    rate=request.POST.get('rate')
    purchaseorderdetail=PurchaseOrderDetailTable(pd_id=pdid,po_id=poid,p_id=pid,length=length,lengthu_id=lengthuid,quantity=quantity,rate=rate)
    purchaseorderdetail.save()
    return redirect("/purchaseorderdetaillist/")
def purchaseorderdetailedit(request,id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    purchaseorder=PurchaseOrderTable.objects.all()
    product=ProductTable.objects.all()
    unit=UnitTable.objects.all()
    purchaseorderdetail=PurchaseOrderDetailTable.objects.get(pd_id=id)
    return render(request,"purchaseorderdetailedit.html",{'purchaseordertables':purchaseorder,'producttable':product,'unittable':unit,'purchaseorderdetail':purchaseorderdetail})



def billingdetaillist(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    bdl=BillingDetailTable.objects.all()
    return render(request,"billingdetaillist.html",{'billingdetailtables':bdl})
def billingdetailadd(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    bill=BillingTable.objects.all()
    product=ProductTable.objects.all()
    return render(request,"billingdetailadd.html",{'billingtables':bill,'producttable':product})
def billingdetailsave(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    if(request.method=="POST"):
        bdid=request.POST.get('bdid')
        bid=request.POST.get('bid')
        pid=request.POST.get('pid')
        bdescription=request.POST.get('ddescription')
        quantity=request.POST.get('quantity')
        rate=request.POST.get('rate')
        billingdetail=BillingDetailTable(bill_d_id=bdid,bill_id=bid,p_id=pid,description=bdescription,quantity=quantity,rate=rate)
        billingdetail.save()
        return redirect("/billingdetaillist/")
def billingdetaildel(request,id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    billingdetail=BillingDetailTable.objects.get(bill_d_id=id)
    billingdetail.delete()
    return redirect("/billingdetaillist/")
def billingdetailupdate(request,id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    bdid=request.POST.get('bdid')
    bid=request.POST.get('bid')
    pid=request.POST.get('pid')
    bdescription=request.POST.get('ddescription')
    quantity=request.POST.get('quantity')
    rate=request.POST.get('rate')
    billingdetail=BillingDetailTable(bill_d_id=bdid,bill_id=bid,p_id=pid,description=bdescription,quantity=quantity,rate=rate)
    billingdetail.save()
    return redirect("/billingdetaillist/")
def billingdetailedit(request,id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    bill=BillingTable.objects.all()
    product=ProductTable.objects.all()
    billingdetail=BillingDetailTable.objects.get(bill_d_id=id)
    return render(request,"billingdetailedit.html",{'billingtables':bill,'producttable':product,'billingdetail':billingdetail})



def salesorderdetaillist(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    sod=SalesOrderDetailTable.objects.all()
    return render(request,"salesorderdetaillist.html",{'salesorderdetailtables':sod})
def salesorderdetailadd(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    salesorder=SalesOrderTable.objects.all()
    product=ProductTable.objects.all()
    unit=UnitTable.objects.all()
    return render(request,"salesorderdetailadd.html",{'salesordertables':salesorder,'producttable':product,'unittable':unit})
def salesorderdetailsave(request):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    if(request.method=="POST"):
        sdid=request.POST.get('sdid')
        soid=request.POST.get('soid')
        pid=request.POST.get('pid')
        length=request.POST.get('length')
        lengthuid=request.POST.get('lengthuid')
        quantity=request.POST.get('quantity')
        rate=request.POST.get('rate')
        simage=request.FILES['image']
        fss=FileSystemStorage()
        file=fss.save(simage.name,simage)
        fileurl=fss.url(file)
        salesorderdetail=SalesOrderDetailTable(sd_id=sdid,so_id=soid,p_id=pid,length=length,lengthu_id=lengthuid,quantity=quantity,rate=rate,image=fileurl)
        salesorderdetail.save()
        return redirect("/salesorderdetaillist/")
def salesorderdetaildel(request,id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    salesorderdetail=SalesOrderDetailTable.objects.get(sd_id=id)
    salesorderdetail.delete()
    return redirect("/salesorderdetaillist/")
def salesorderdetailupdate(request,id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    sdid=request.POST.get('sdid')
    soid=request.POST.get('soid')
    pid=request.POST.get('pid')
    length=request.POST.get('length')
    diameter=request.POST.get('diameter')
    lengthuid=request.POST.get('lengthuid')
    quantity=request.POST.get('quantity')
    rate=request.POST.get('rate')
    simage=request.FILES['image']
    fss=FileSystemStorage()
    file=fss.save(simage.name,simage)
    fileurl=fss.url(file)
    salesorderdetail=SalesOrderDetailTable(sd_id=sdid,so_id=soid,p_id=pid,length=length,diameter=diameter,quantity=quantity,rate=rate,image=fileurl)
    salesorderdetail.save()
    return redirect("/salesorderdetaillist/")
def salesorderdetailedit(request,id):
    if request.session.has_key('admin'):
        pass
    else:
        return redirect("/login/")
    salesorder=SalesOrderTable.objects.all()
    product=ProductTable.objects.all()
    unit=UnitTable.objects.all()
    salesorderdetail=SalesOrderDetailTable.objects.get(sd_id=id)
    return render(request,"salesorderdetailedit.html",{'salesordertables':salesorder,'producttable':product,'unittable':unit,'salesorderdetail':salesorderdetail})


def unitshow(request):
    return render(request,"unit.html")

def login(request):
    if request.method=="POST":
        email=request.POST.get('Email')
        pwd=request.POST.get('Password')
        
        admins=Admin.objects.filter(email_id=email,password=pwd)
        i=0
        for a in admins:
            i=i+1
            request.session['admin']=a.admin_name
            return redirect("/adminlist/")
            
    return render(request,"login.html")
    
def visitor(request):
    prt=ProductTable.objects.all()
    return render(request,"visitor/visitorhome.html",{'producttables':prt})

def productdetail(request,id):
    prd=ProductTable.objects.get(p_id=id)
    units=UnitTable.objects.all()
    return render(request,"visitor/productdetail.html",{'producttables':prd,'units':units})

def registration(request):
    if request.method=="POST":
        cname=request.POST.get('cname')
        caddress=request.POST.get('caddress')
        ccontact=request.POST.get('ccontact')
        pwd=request.POST.get('cpassword')
        email=request.POST.get('cemailid')
        pin=request.POST.get('cpincode')
        area=Area.objects.get(pincode=pin)
        customer=Customer(customer_name=cname,customer_address=caddress,contact_no_field=ccontact,password=pwd,email_id=email,pincode=area)
        customer.save()
        return redirect("/clogin/")
        
    pincodes=Area.objects.all()
    return render(request,"visitor/registration.html",{'areas':pincodes})

def addtocart(request):
    if request.method=="POST":
        if request.session.has_key('customer'):
            custid=request.session.get('customer')
            request.session.has_key('producttable')
            pid=request.POST.get('pid')
            prod=ProductTable.objects.get(p_id=pid)
            length=request.POST.get('length')
            # lengthu=request.POST.get('lengthu')
            diameter=request.POST.get('diameter')
            # diameteru=request.POST.get('diameteru')
            rate=float(prod.rate_per_mm)
            rate=float(rate)
            ld=float(length)+float(diameter)
            ld=float(ld)
            if ld>0.0 and ld<150.0:
                rate=rate*1.3
            elif ld>=150.0 and ld<200.0:
                rate=rate*2.5
            elif ld>=200 and ld<300:
                rate=rate*4.5
            elif ld>=300 and ld<400:
                rate=rate*5.5
            elif ld>=400 and ld<500:
                rate=rate*6.5
            elif ld>=500 and ld<650:
                rate=rate*7.8
            quantity=request.POST.get('quantity')
            #image=request.POST.get('image')
            cust=Customer.objects.get(cust_id=custid)
            # lunit=UnitTable.objects.get(unit_id=lengthu)
            # dunit=UnitTable.objects.get(unit_id=diameteru)
            tot=float(quantity)*rate
            cart=Cart(cust=cust,p=prod,length=length,diameter=diameter,quantity=quantity,rate=rate,total=tot)
            cart.save()
            return redirect("/showcart/")
        else:
            return redirect("/clogin/")
        
    return redirect("/visitorhome/")
    

def showcart(request):
    custid=request.session.get('customer')
    cust=Customer.objects.get(cust_id=custid)
    carts=Cart.objects.filter(cust=cust)
    sum=0
    for cart in carts:
        sum=sum+cart.total

    return render(request,"visitor/showcart.html",{'carts':carts,'total':sum})

def checkout(request):
    custid=request.session.get('customer')
    cust=Customer.objects.get(cust_id=custid)
    carts=Cart.objects.filter(cust=cust)
    dt=datetime.now()
    sum=0
    for cart in carts:
        sum=sum+cart.total
    so=SalesOrderTable(cust=cust,sales_date=dt,total=sum)
    so.save()
    
    for cart in carts:
        sod=SalesOrderDetailTable(so=so,p=cart.p,length=cart.length,diameter=cart.diameter,quantity=cart.quantity,rate=cart.rate)
        sod.save()
    for cart in carts:
        cart.delete()
    #return redirect("/salesorderlist/")
    return render(request,"visitor/showcart.html",{'carts':carts,'total':sum})

def deletecart(request,id):
    cart=Cart.objects.get(cart_id=id)
    cart.delete()
    return redirect("/showcart/")

def clogin(request):
    if request.method=="POST":
        email=request.POST.get('cemailid')
        pwd=request.POST.get('cpassword')
        
        customers=Customer.objects.filter(email_id=email,password=pwd)
        i=0
        for a in customers:
            i=i+1
            request.session['customer']=a.cust_id
            return redirect("/visitorhome/")
            
    return render(request,"visitor/clogin.html")


def contactus(request):
    return render(request,"visitor/contactus.html")
def aboutus(request):
    return render(request,"visitor/aboutus.html")

def profile(request):
    if request.session.has_key('customer'):
        pass
    else:
        return redirect("/clogin/")
    areas=Area.objects.all()
    custid=request.session.get('customer')
    cust=Customer.objects.get(cust_id=custid)
    return render(request,"visitor/profile.html",{'areas':areas,'customer':cust})
def updateprofile(request):
    if request.session.has_key('customer'):
        pass
    else:
        return redirect("/clogin/")
    cid=request.POST.get('cid')
    cname=request.POST.get('cname')
    caddress=request.POST.get('caddress')
    ccontact=request.POST.get('ccontact')
    cpassword=request.POST.get('cpassword')
    cemailid=request.POST.get('cemailid')
    cpincode=request.POST.get('cpincode')
    area=Area.objects.get(pincode=cpincode)
    customer=Customer(cust_id=cid,customer_name=cname,customer_address=caddress,contact_no_field=ccontact,password=cpassword,email_id=cemailid,pincode=area)
    customer.save()
    return redirect("/visitorhome/")

def myorders(request):
    if request.session.has_key('customer'):
        pass
    else:
        return redirect("/clogin/")
    custid=request.session.get('customer')
    cust=Customer.objects.get(cust_id=custid)
    slo=SalesOrderTable.objects.filter(cust=cust)
    sod=[]
    return render(request,"visitor/myorders.html",{'salesorders':slo,'salesorderdetailtables':sod})

def myordersd(request,id):
    if request.session.has_key('customer'):
        pass
    else:
        return redirect("/clogin/")
    sod=SalesOrderDetailTable.objects.filter(so_id=id)
    custid=request.session.get('customer')
    cust=Customer.objects.get(cust_id=custid)
    slo=SalesOrderTable.objects.filter(cust=cust)
    return render(request,"visitor/myorders.html",{'salesorders':slo,'salesorderdetailtables':sod})
