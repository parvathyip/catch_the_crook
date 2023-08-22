from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib import messages
from random import randint, randrange
from .models import *
# Create your views here.
def index(request):
    return render(request,'index.html')
def users_login(request):
    msg=""
    if request.POST:
        email=request.POST['email']
        request.session['email']=email
        pass1=request.POST['password']
        user=authenticate(username=email,password=pass1)
        if user is not None:
            if user.user_type=='admin':
                return redirect('/admin-dashboard')
            elif user.user_type=='dgp':
                return redirect('/dgp-dashboard')
            elif user.user_type=='station':
                msg="login success"
                messages.info(request,msg)
                return redirect('/station-dashboard')
            # elif user.user_type=='public':
            #     # msg="login success"
            #     # messages.info(request,msg)
            #     return redirect('/public-dashboard')
            elif user.user_type=='users':
                msg="login success"
                messages.info(request,msg)
                return redirect('/public-dashboard')
        else:
            msg="username or password invalid"
            messages.info(request,msg)      
    return render(request,'users_login.html')
#admin
def admin_dashboard(request):
    return render(request,'admin/admin_dashboard.html')
def admin_adddgp(request):
    if request.POST:
        firstname=request.POST['fname']
        lastname=request.POST['lname']
        phone=request.POST['phone']
        dgpimage=request.POST.get('dgpimage')
        dgpimg_name=request.FILES['dgpimage']
        job_status=request.POST['job_status']
        office=request.POST['address']
        ofc_district=request.POST['office_district']
        email=request.POST['email']
        password=request.POST['password']
        log_user=Login_Table.objects.create_user(user_type="dgp",view_password=password,password=password,username=email)
        log_user.save()
        add_dgp=Register_dgp.objects.create(fname=firstname,lname=lastname,phone=phone,image=dgpimg_name,job_status=job_status,office_address=office,office_district=ofc_district,email=email,user_login=log_user)
        add_dgp.save()
    return render(request,'admin/admin_adddgp.html')
def admin_viewdgp(request):
    dgps=Register_dgp.objects.all()
    return render(request,'admin/admin_viewdgp.html',{"dgps":dgps})
# def admin_updatedgp(request):
#     id=request.GET.get('id')
#     update_obj=Register_dgp.objects.filter(id=id)
#     # print(update_obj)
#     if request.POST:
#         firstname=request.POST['fname']
#         lastname=request.POST['lname']
#         phone=request.POST['phone']
#         dgpimage=request.POST.get('dgpimage')
#         dgpimg_name=request.FILES['dgpimage']
#         job_status=request.POST['job_status']
#         office=request.POST['address']
#         ofc_district=request.POST['office_district']
#         dgp=Register_dgp.objects.get(id=id)
#         dgp.fname=firstname
#         dgp.lname=lastname
#         dgp.phone=phone
#         dgp.image=dgpimg_name
#         dgp.job_status=job_status
#         dgp.office_address=office
#         dgp.office_district=ofc_district
#         dgp.save()
#     return render(request,'admin/admin_updatedgp.html',{'dgp':update_obj})
def admin_deletedgp(request):
    id=request.GET.get('id')
    del_obj=Register_dgp.objects.get(id=id).delete()
    return redirect('/admin-viewdgp')
#dgp
def dgp_dashboard(request):
    return render(request,'dgp/dgp_dashboard.html')
def dgp_addstation(request):
    if request.POST:
        s_name=request.POST['name']
        s_phone=request.POST['phone']
        s_address=request.POST['address']
        s_email=request.POST['email']
        s_password=request.POST['password']
        dgp_email=request.session['email']
        dgp_obj=Register_dgp.objects.get(email=dgp_email)
        log_user=Login_Table.objects.create_user(user_type="station",view_password=s_password,password=s_password,username=s_email)
        log_user.save()
        add_station=Register_station.objects.create(station_name=s_name,phone=s_phone,office_address=s_address,email=s_email,user_login=log_user,dgp=dgp_obj)
        add_station.save()
    return render(request,'dgp/dgp_addstation.html')
def dgp_viewprofile(request):
    email=request.session['email']
    # print(email,'############################')
    dgp_id=Register_dgp.objects.filter(email=email)
    # print(dgp_id,'###########################')
    return render(request,'dgp/dgp_viewprofile.html',{'dgp':dgp_id})

def dgp_updatedgp(request):
    id=request.GET.get('id')
    update_obj=Register_dgp.objects.filter(id=id)
    # print(update_obj)
    if request.POST:
        firstname=request.POST['fname']
        lastname=request.POST['lname']
        phone=request.POST['phone']
        dgpimage=request.POST.get('dgpimage')
        dgpimg_name=request.FILES['dgpimage']
        job_status=request.POST['job_status']
        office=request.POST['address']
        ofc_district=request.POST['office_district']
        dgp=Register_dgp.objects.get(id=id)
        dgp.fname=firstname
        dgp.lname=lastname
        dgp.phone=phone
        dgp.image=dgpimg_name
        dgp.job_status=job_status
        dgp.office_address=office
        dgp.office_district=ofc_district
        dgp.save()
    return render(request,'dgp/dgp_updatedgp.html',{"dgp":update_obj})
def dgp_viewhistories(request):
    closed_case=Add_complaint.objects.filter(complaint_status="Closed")
    print(closed_case)
    return render(request,'dgp/dgp_viewhistories.html',{'histories':closed_case})
#station
def station_dashboard(request):
    return render(request,'station/station_dashboard.html')
def station_addwantedcriminal(request):
    station_email=request.session['email']
    station_obj=Register_station.objects.get(email=station_email)
    if request.POST:
        images=request.FILES.getlist('images')
        fname=request.POST['fname']
        lname=request.POST['lname']
        fathername=request.POST['fathername']
        age=request.POST['age']
        sex=request.POST['sex']
        address=request.POST['address']
        crimemode=request.POST['crime_mode']
        crimedesc=request.POST['crime_desc']
        reg_wanted=Register_wanted.objects.create(fname=fname,lname=lname,father_name=fathername,age=age,
                                                  sex=sex,address=address,mode_of_crime=crimemode,crime_desc=crimedesc,station=station_obj)
        reg_wanted.save()
        for image in images:
            image=Wanted_images.objects.create(wanted=reg_wanted,wanted_images=image)
            image.save()
        
    return render(request,'station/station_addwantedcriminal.html')


def station_viewcomplaints(request):
    station_email=request.session['email']
    # print(station_email)
    stationobj=Register_station.objects.get(email=station_email)
    # print(stationobj)
    stationdgp=stationobj.dgp
    # print(stationdgp.office_district,"##################")
    publics=Register_public.objects.filter(district=stationdgp.office_district)
    # print(publics,"############################")
    complaints=Add_complaint.objects.filter(complaint_status="Pending",complaint_type_status='complaint',public_id__district=stationdgp.office_district)
    # print(complaints,'################')
    return render(request,'station/station_viewcomplaints.html',{'complaints':complaints})


def station_viewmissings(request):
    return render(request,'station/station_viewmissings.html')

def station_registercomplaint(request):
    id=request.GET.get('id')
    c_status=request.GET.get('complaint_status')
    new_status=Add_complaint.objects.filter(id=id,complaint_status=c_status).update(complaint_status="Registered")
    return redirect('/station-viewcomplaints')
def station_withdrawcomplaint(request):
    id=request.GET.get('id')
    email=request.session['email']
    sobj=Register_station.objects.get(email=email)
    c_status=request.GET.get('complaint_status')
    new_status=Add_complaint.objects.filter(id=id,complaint_status=c_status).update(complaint_status="Withdrawed",station=sobj)
    return redirect('/station-viewcomplaints')
def station_viewwithdrawed(request):
    email=request.session['email']
    sobj=Register_station.objects.get(email=email)
    withdraweds=Add_complaint.objects.filter(station=sobj,complaint_status="Withdrawed")
    # print(withdraweds,'###########################################*******')
    return render(request,'station/station_viewwithdrawed.html',{"withdraweds":withdraweds})
def station_viewregistered(request):
    p_email=request.session['email']
    # print(p_email,'#############################')
    p_obj=Register_station.objects.get(email=p_email)
    # print(p_obj.dgp,'pobj.dgp')
    dgp=Register_dgp.objects.get(id=p_obj.dgp.id)
    # print(dgp.office_district,'district#################')
    reg_complaints=Add_complaint.objects.filter(complaint_status="Registered",public__district=dgp.office_district)
    # print(reg_complaints,'registered###################')
    return render(request,'station/station_viewregistered.html',{'reg_complaints':reg_complaints})
def station_viewcriminals(request):
    criminals=Register_wanted.objects.filter(wanted_status="wanted")
    # print(criminals,"#########################")
    return render(request,'station/station_viewcriminals.html',{'criminals':criminals})
def station_viewcriminaldetail(request):
    criminal_id=request.GET.get('id')
    criminal_obj=Register_wanted.objects.get(id=criminal_id)
    criminal_images=Wanted_images.objects.filter(wanted=criminal_obj)
    # print(criminal_images)
    criminal_detail=Register_wanted.objects.get(id=criminal_obj.id)
    feedbacks=Public_feedback.objects.filter(wanted=criminal_obj)
    # print(feedbacks)
    return render(request,'station/station_viewcriminaldetail.html',{'criminal_images':criminal_images,'details':criminal_detail,'feedbacks':feedbacks})
def station_searchcriminal(request):
    cid=request.GET.get('id')
    # randomcid=request.GET.get('complaintid')
    crimemode=request.GET.get('crime_mode')
    # print(cid,randomcid,crimemode,"################new")
    similarmode=Register_wanted.objects.filter(mode_of_crime=crimemode)
    # print(similarmode,"555555555555555555")
    return render(request,'station/station_searchcriminal.html',{"similarcriminals":similarmode,'complaint':cid})
def station_viewsearchcriminaldetail(request):
    complaint=request.GET.get('complaintid')
    # print(com_random_no,'$$$$$$$$$$$$$$$$$$$$$$$$')
    criminal_id=request.GET.get('wanteddataid')
    criminal_obj=Register_wanted.objects.get(id=criminal_id)
    criminal_images=Wanted_images.objects.filter(wanted=criminal_obj)
    # print(criminal_images)
    criminal_detail=Register_wanted.objects.get(id=criminal_obj.id)
    return render(request,'station/station_viewsearchcriminaldetail.html',{'criminal_images':criminal_images,'details':criminal_detail,'complaintid':complaint})

def station_arrest(request):
    criminalid=request.GET.get('criminalid')
    complaintid=request.GET.get('complaintid')
    station_email=request.session['email']
    stationobj=Register_station.objects.get(email=station_email)
    criminalobj=Register_wanted.objects.get(id=criminalid)
    # print(criminalid,stationobj,'***********************************')
    complaintobj=Add_complaint.objects.filter(id=complaintid).update(complaint_status="arrested",station=stationobj,criminal=criminalobj)
    # print(complaintobj,":):):):):)")
    criminal_status=Register_wanted.objects.filter(id=criminalid).update(wanted_status="arrested")
    # print(criminal_status,":(:(:(:(")
    return redirect('/station-viewregistered')
def station_viewarrested(request):
    semail=request.session['email']
    sobj=Register_station.objects.get(email=semail)
    arrests=Add_complaint.objects.filter(station=sobj,complaint_status='arrested')
    # print(arrests,'@@@@@@@@@@@@@@@@@@@@@@')
    return render(request,'station/station_viewarrested.html',{"arrests":arrests})
def station_addwitness(request):
    cid=request.GET.get('cid')
    # print(cid,'###########')
    # cobj=Add_complaint.objects.get(id=cid)
    if request.POST:
        fname=request.POST['wfname']
        lname=request.POST['wlname']
        phone=request.POST['wphone']
        email=request.POST['wemail']
        district=request.POST['wdistrict']
        # print(fname,lname,phone,email,district)
        c_witness=Add_complaint.objects.filter(id=cid).update(witness_district=district,witness_email=email,witness_fname=fname,witness_lname=lname,witness_phone=phone)
        # print(c_witness)
        return redirect('/station-viewarrested')
    return render(request,'station/station_addwitness.html')
def station_missings(request):
    missings=Add_complaint.objects.filter(complaint_type_status="missing")
    return render(request,'station/station_viewmissings.html',{"missings":missings})
def station_closecase(request):
    cid=request.GET.get('cid')
    closed=Add_complaint.objects.filter(id=cid).update(complaint_status="Closed")
    return redirect('/station-viewarrested')

def station_viewclosed(request):
    email=request.session['email']
    sobj=Register_station.objects.get(email=email)
    closed=Add_complaint.objects.filter(station=sobj,complaint_status="Closed")
    # print(closed)
    if request.POST:
        pdffilename=request.FILES['fir_upload']
        compid=request.POST['compid']
        print(pdffilename)
        fir_add=Add_complaint.objects.get(id=compid)
        fir_add.fir_upload=pdffilename
        fir_add.save()
        # fir_add.save()
        
        print(fir_add,":)))))))))))))")
    return render(request,'station/station_viewclosed.html',{'closed':closed})

#public
def public_dashboard(request):
    return render(request,'public/public_dashboard.html')
def public_addcomplaint(request):
    public_email=request.session['email']
    public_obj=Register_public.objects.get(email=public_email)
    if request.POST:
        # date=request.POST['missingdate']
        mode=request.POST['crime_mode']
        desc=request.POST['crimedesc']        
        complaintid =randint(100, 999) 
        # print(complaintid,"############################")
        mdata=Add_complaint.objects.create(missing_image="",missing_desc="",
                                           crime_mode=mode,crime_desc=desc,complaint_type_status='complaint',complaintid=complaintid,public=public_obj)
        mdata.save()
        msge="your complaint has been send with complaint id: "+str(complaintid)
        messages.info(request,msge)
    return render(request,'public/public_addcomplaint.html')
def public_addmissing(request):
    public_email=request.session['email']
    public_obj=Register_public.objects.get(email=public_email)
    # public_id=public_obj.id
    if request.POST:
        # date=request.POST['missingdate']
        image=request.POST.get('missingimage')
        imgname=request.FILES['missingimage']
        desc=request.POST['missingdesc']
        
        complaintid =randint(100, 999) 
        # print(complaintid,"############################")
        mdata=Add_complaint.objects.create(missing_image=imgname,missing_desc=desc,
                                           crime_mode='',crime_desc='',complaintid=complaintid,public=public_obj)
        mdata.save()
        msge="your complaint has been send with complaint id: "+str(complaintid)
        messages.info(request,msge)
    return render(request,'public/public_addmissing.html')
def public_register(request):
    if request.POST:
        firstname=request.POST['fname']
        lastname=request.POST['lname']
        phone=request.POST['phone']
        email=request.POST['email']
        password=request.POST['password']
        user_login=Login_Table.objects.create_user(user_type="users",view_password=password,username=email,password=password)
        user_login.save()
        add_public=Register_public.objects.create(f_name=firstname,l_name=lastname,phone=phone,email=email,user_login=user_login)
        add_public.save()
        return redirect('/users-login')
    return render(request,'public/public_register.html')
def public_viewcomplaints(request):
    public_email=request.session['email']
    public_obj=Register_public.objects.get(email=public_email)
    public_id=public_obj.id
    complaints=Add_complaint.objects.filter(public_id=public_id)
    # print(complaints)
    return render(request,'public/public_viewcomplaints.html',{"complaints":complaints})

def public_viewcriminals(request):
    criminals=Register_wanted.objects.filter(wanted_status="wanted")
    return render(request,'public/public_viewcriminals.html',{'criminals':criminals})

def public_viewcriminaldetail(request):
    criminal_id=request.GET.get('id')
    criminal_obj=Register_wanted.objects.get(id=criminal_id)
    criminal_images=Wanted_images.objects.filter(wanted=criminal_obj)
    # print(criminal_images)
    criminal_detail=Register_wanted.objects.get(id=criminal_obj.id)
    return render(request,'public/public_viewcriminaldetail.html',{'criminal_images':criminal_images,'details':criminal_detail})
def public_haveaccount(request):
    return redirect('/users-login')
def public_newmissingcase(request):
    if request.POST:
        firstname=request.POST['fname']
        lastname=request.POST['lname']
        phone=request.POST['phone']
        email=request.POST['email']
        password=request.POST['password']
        district=request.POST['district']
        user_login=Login_Table.objects.create_user(user_type="users",view_password=password,username=email,password=password)
        user_login.save()
        add_public=Register_public.objects.create(f_name=firstname,l_name=lastname,phone=phone,email=email,district=district,user_login=user_login)
        add_public.save()
        request.session['id']=add_public.id
        # print(request.session['id'])
        pid=request.session['id']
        # print(pid,"#################")
        public_obj=Register_public.objects.get(id=pid)
        # print(public_obj,'################')
        image=request.POST.get('missingimage')
        imgname=request.FILES['missingimage']
        desc=request.POST['missingdesc']
        complaintid =randint(100, 999) 
        # print(complaintid,"############################")
        mdata=Add_complaint.objects.create(missing_image=imgname,missing_desc=desc,
                                           crime_mode='',crime_desc='',complaint_type_status='missing',complaintid=complaintid,public=public_obj)
        mdata.save()
        msge="your complaint has been send with complaint id: "+str(complaintid)
        messages.info(request,msge)
    return render(request,'public_newmissingcase.html')
 
def public_newcomplaintcase(request):
    if request.POST:
        firstname=request.POST['fname']
        lastname=request.POST['lname']
        phone=request.POST['phone']
        email=request.POST['email']
        password=request.POST['password']
        district=request.POST['district']
        user_login=Login_Table.objects.create_user(user_type="users",view_password=password,username=email,password=password)
        user_login.save()
        add_public=Register_public.objects.create(f_name=firstname,l_name=lastname,phone=phone,email=email,district=district,user_login=user_login)
        add_public.save()
        request.session['id']=add_public.id
        # print(request.session['id'])
        pid=request.session['id']
        # print(pid,"#################")
        public_obj=Register_public.objects.get(id=pid)
        # print(public_obj,'################')
        mode=request.POST['crime_mode']
        desc=request.POST['crimedesc']  
        complaintid =randint(100, 999) 
        # print(complaintid,"############################")
        mdata=Add_complaint.objects.create(missing_image="",missing_desc="",
                                           crime_mode=mode,crime_desc=desc,complaint_type_status='complaint',complaintid=complaintid,public=public_obj)
        mdata.save()
        msge="your complaint has been send with complaint id: "+str(complaintid)
        messages.info(request,msge)
    return render(request,'public_newcomplaintcase.html')

def public_addfeedback(request):
    cid=request.GET.get('cid')
    cobj=Register_wanted.objects.get(id=cid)
    # print(cobj)
    pemail=request.session['email']
    pobj=Register_public.objects.get(email=pemail)
    # print(pobj)
    if request.POST:
        feedback=request.POST['feedback']
        # print(feedback)
        feed=Public_feedback.objects.create(feedback=feedback,public=pobj,wanted=cobj)
        feed.save()
        # print(feed)
    return render(request,'public/public_addfeedback.html')
def public_viewfeedbacks(request):
    email=request.session['email']
    pobj=Register_public.objects.get(email=email)
    # print(pobj)
    feedbacks=Public_feedback.objects.filter(public=pobj)
    # print(feedbacks)

    return render(request,'public/public_viewfeedbacks.html',{'feedbacks':feedbacks})