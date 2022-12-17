from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from topy.models import *
from django.http.response import JsonResponse
from rest_framework.generics import get_object_or_404
from pyzipcode import ZipCodeDatabase
#--------------------------Login-------------------------------------


@api_view(['GET'])
def login(request, email, password):
    if request.method == 'GET':
        user = User.objects.filter(email=email, password=password)
        serializer = UserSerializer(user, many=True)
    return JsonResponse(serializer.data, safe=False)
#--------------------------UserType-------------------------------------
@api_view(['GET'])
def get_usertype(request):
    if request.method == 'GET':
        usertype = UserType.objects.all()
        serializer = UserTypeSerializer(usertype, many=True)
        return JsonResponse(serializer.data, safe=False)

#--------------------------Activity-------------------------------------
@api_view(['GET'])
def get_activity_senior_citizen(request):
    if request.method == 'GET':
        activity = Activity.objects.filter(user_type=1)
        serializer = ActivitySerializer(activity, many=True)
        return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def get_activity_child(request):
    if request.method == 'GET':
        activity = Activity.objects.filter(user_type=2)
        serializer = ActivitySerializer(activity, many=True)
        return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def get_activity_pet(request):
    if request.method == 'GET':
        activity = Activity.objects.filter(user_type=3)
        serializer = ActivitySerializer(activity, many=True)
        return JsonResponse(serializer.data, safe=False)

#--------------------------User details-------------------------------------
@api_view(['GET','PUT'])
def user_details(request, id):
    if request.method == 'GET':
        user_details = User.objects.filter(user_id=id)
        serializer = UserSerializer(user_details, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'PUT':
        queryset = User.objects.all()
        update_data = get_object_or_404(queryset, user_id=id)
        serializer = UserSerializer(update_data, data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
        return JsonResponse(serializer.data, safe=False)

@api_view(['POST'])
def add_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            temp = serializer.data
            # print("USER TYPE" ,temp["user_type"])
            type = temp["user_type"]
            if type == 1:
                new_senior = {
                    "name": temp["name"],
                    "gender": "",
                    "birthday": None,
                    "want_pet": True,
                    "want_child": True,
                    "about_me": "",
                    "emergency_contact": "",
                    "user_type": "1",
                    "user": temp["user_id"],
                    "activity_pref": []
                }
                serializer_senior = SeniorCitizenSerializer(data=new_senior)
                if serializer_senior.is_valid():
                    serializer_senior.save()
        return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def get_all_users(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)

#--------------------------Senior citizen details-------------------------------------
@api_view(['GET'])
def get_all_senior_citizens(request):
    if request.method == 'GET':
        senior_citizens = SeniorCitizen.objects.all()
        serializer = SeniorCitizenSerializer(senior_citizens, many=True)
        temp = serializer.data
        for one in temp:
            activity_name = []
            activity_prefs = one['activity_pref']
            # print("ACTIVITIES ARE :",activity_prefs)
            for activ in activity_prefs:
                name = Activity.objects.get(activity_id=activ).name
                activity_name.append(name)
            one['activity_pref'] = activity_name
            # print(one)
        return JsonResponse(temp, safe=False)


@api_view(['GET', 'PUT'])
def senior_citizen_details(request, id):
    if request.method == 'GET':
        senior_citizen_details = SeniorCitizen.objects.filter(senior_citizen_id=id)
        serializer = SeniorCitizenSerializer(senior_citizen_details, many=True)
        temp = serializer.data
        for one in temp:
            activity_name = []
            activity_prefs = one['activity_pref']
            # print("ACTIVITIES ARE :",activity_prefs)
            for activ in activity_prefs:
                name = Activity.objects.get(activity_id=activ).name
                activity_name.append(name)
            one['activity_pref'] = activity_name
            # print(one)
        return JsonResponse(temp, safe=False)
    elif request.method == 'PUT':
        queryset = SeniorCitizen.objects.all()
        update_data = get_object_or_404(queryset, senior_citizen_id=id)
        serializer = SeniorCitizenSerializer(update_data, data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
        return JsonResponse(serializer.data,safe = False)

@api_view(['POST'])
def add_senior_citizen(request):
    if request.method == 'POST':
        serializer = SeniorCitizenSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return JsonResponse(serializer.data, safe=False)

@api_view(['GET','PUT'])
def get_my_senior_citizen(request, id):
    if request.method == 'GET':
        senior_details = SeniorCitizen.objects.filter(user=id)
        serializer_senior = SeniorCitizenSerializer(senior_details, many=True)
        temp = serializer_senior.data
        for one in temp:
            activity_name = []
            activity_prefs = one['activity_pref']
            # print("ACTIVITIES ARE :",activity_prefs)
            for activ in activity_prefs:
                name = Activity.objects.get(activity_id = activ).name
                activity_name.append(name)
            one['activity_pref']   = activity_name
            # print(one)
        return JsonResponse(temp,safe=False)


#--------------------------Child details-------------------------------------
@api_view(['GET'])
def get_all_children(request):
    if request.method == 'GET':
        children = Child.objects.all()
        serializer = ChildSerializer(children, many=True)
        temp = serializer.data
        for one in temp:
            activity_name = []
            activity_prefs = one['activity_pref']
            # print("ACTIVITIES ARE :",activity_prefs)
            for activ in activity_prefs:
                name = Activity.objects.get(activity_id=activ).name
                activity_name.append(name)
            one['activity_pref'] = activity_name
            # print(one)
        return JsonResponse(temp, safe=False)

@api_view(['GET','PUT'])
def child_details(request, id):
    if request.method == 'GET':
        child_details = Child.objects.filter(child_id=id)
        serializer = ChildSerializer(child_details, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'PUT':
        queryset = Child.objects.all()
        update_data = get_object_or_404(queryset, child_id=id)
        serializer = ChildSerializer(update_data, data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
        return JsonResponse(serializer.data, safe=False)

@api_view(['POST'])
def add_child(request):
    if request.method == 'POST':
        serializer = ChildSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return JsonResponse(serializer.data, safe=False)


@api_view(['GET','PUT'])
def get_my_childs(request, id):
    if request.method == 'GET':
        child_details = Child.objects.filter(user=id)
        serializer_child = ChildSerializer(child_details, many=True)
        temp = serializer_child.data
        for one in temp:
            activity_name = []
            activity_prefs = one['activity_pref']
            # print("ACTIVITIES ARE :",activity_prefs)
            for activ in activity_prefs:
                name = Activity.objects.get(activity_id = activ).name
                activity_name.append(name)
            one['activity_pref']   = activity_name
            # print(one)
        return JsonResponse(temp,safe=False)

#--------------------------Pet details-------------------------------------
@api_view(['GET'])
def get_all_pets(request):
    if request.method == 'GET':
        pets = Pet.objects.all()
        serializer = PetSerializer(pets, many=True)
        return JsonResponse(serializer.data, safe=False)

@api_view(['GET','PUT'])
def pet_details(request, id):
    if request.method == 'GET':
        pet_details = Pet.objects.filter(pet_id=id)
        serializer = ChildSerializer(pet_details, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'PUT':
        queryset = Pet.objects.all()
        update_data = get_object_or_404(queryset, pet_id=id)
        serializer = PetSerializer(update_data, data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
        return JsonResponse(serializer.data, safe=False)

@api_view(['POST'])
def add_pet(request):
    if request.method == 'POST':
        serializer = PetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return JsonResponse(serializer.data, safe=False)

@api_view(['GET','PUT'])
def get_my_pets(request, id):
    if request.method == 'GET':
        child_details = Pet.objects.filter(user=id)
        serializer_child = PetSerializer(child_details, many=True)
        temp = serializer_child.data
        for one in temp:
            activity_name = []
            activity_prefs = one['activity_pref']
            # print("ACTIVITIES ARE :",activity_prefs)
            for activ in activity_prefs:
                name = Activity.objects.get(activity_id = activ).name
                activity_name.append(name)
            one['activity_pref']   = activity_name
            # print(one)
        return JsonResponse(temp, safe=False)

#--------------------------TOPY Stations-------------------------------------
@api_view(['GET'])
def get_topystations(request):
    if request.method == 'GET':
        topystations = TOPYStation.objects.all()
        serializer = TOPYStationSerializer(topystations, many=True)
        return JsonResponse(serializer.data, safe=False)

#--------------------------Match details-------------------------------------
@api_view(['GET'])
def get_matchs_incoming(request, id):
    if request.method == 'GET':
        response_list = []
        final = set()
        user_type_value = User.objects.get(user_id=id).user_type.user_type_id
        if user_type_value == 1:
            senior_list = []
            seniors = SeniorCitizen.objects.filter(user=id)
            for senior in seniors:
                senior_list.append(senior.senior_citizen_id)
            final = Match.objects.filter(senior_citizen__in = senior_list, status="Pending", initiator_type=2)
        else:
            child_list = []
            pet_list = []
            childs = Child.objects.filter(user=id)
            child_serializer = ChildSerializer(childs, many=True)
            child_data = child_serializer.data
            for child in child_data:
                child_list.append(child['child_id'])
            child_matchs = Match.objects.filter(child__in=child_list, status="Pending", initiator_type=1)
            for child in child_matchs:
                final.add(child)
            # for pet in pet_matchs:
            #     final.add(pet)
        serializer = MatchSerializer(final, many=True)
        temp = serializer.data
        for one in temp:
            # senior_name = SeniorCitizen.objects.get(senior_citizen_id=one['senior_citizen']).user.name
            senior_details = SeniorCitizen.objects.get(senior_citizen_id=one['senior_citizen'])
            child_details = Child.objects.get(child_id=one['child'])
            if one["pet"] != None:
                pet_details = Pet.objects.get(pet_id=one['pet'])


            senior_details_serialized = SeniorCitizenSerializer(senior_details)
            activity_name = []
            activity_prefs = senior_details_serialized.data['activity_pref']
            # print("ACTIVITIES ARE :",activity_prefs)
            for activ in activity_prefs:
                name = Activity.objects.get(activity_id=activ).name
                activity_name.append(name)
            print(activity_name)
            senior_final = senior_details_serialized.data
            senior_final['activity_pref'] = activity_name
            # senior_details_serialized.data = temp
            print("SENIOR : ", senior_final)


            child_details_serialized = ChildSerializer(child_details)
            child_final = child_details_serialized.data
            activity_name = []
            activity_prefs = child_final['activity_pref']
            # print("ACTIVITIES ARE :",activity_prefs)
            for activ in activity_prefs:
                name = Activity.objects.get(activity_id=activ).name
                activity_name.append(name)
            child_final['activity_pref'] = activity_name

            if one["pet"] != None:
                pet_details_serialized = PetSerializer(pet_details)
                pet_final = pet_details_serialized.data
                activity_name = []
                activity_prefs = pet_final['activity_pref']
                # print("ACTIVITIES ARE :",activity_prefs)
                for activ in activity_prefs:
                    name = Activity.objects.get(activity_id=activ).name
                    activity_name.append(name)
                pet_final['activity_pref'] = activity_name
            else:
                pet_final = {}

            # child_name = Child.objects.get(child_id=one['child']).name
            # pet_name = Pet.objects.get(pet_id=one['pet']).name
            # print(senior_name,child_name, pet_name)
            newData = {"data": one,
                       "senior_details": senior_final,
                       "child_details": child_final,
                       "pet_details": pet_final}
            response_list.append(newData)
    return JsonResponse(response_list, safe=False)


@api_view(['GET'])
def get_matchs_outgoing(request, id):
    if request.method == 'GET':
        response_list = []
        user_type_value = User.objects.get(user_id = id).user_type.user_type_id
        matchs = Match.objects.filter( user=id,  status="Pending", initiator_type = user_type_value)
        serializer = MatchSerializer(matchs, many=True)
        temp = serializer.data
        for one in temp:
            senior_name = SeniorCitizen.objects.get(senior_citizen_id=one['senior_citizen']).user.name
            child_name = Child.objects.get(child_id=one['child']).name
            if one["pet"] != None:
                pet_name = Pet.objects.get(pet_id=one['pet']).name
            else:
                pet_name = "No Pet"
            # print(senior_name,child_name, pet_name)
            newData = {"data": one,
                       "senior_name": senior_name,
                       "child_name": child_name,
                       "pet_name": pet_name}
            response_list.append(newData)
    return JsonResponse(response_list, safe=False)

@api_view(['GET'])
def get_matchs_past(request, id):
    if request.method == 'GET':
        response_list = []
        final = set()
        user_type_value = User.objects.get(user_id = id).user_type.user_type_id
        if user_type_value == 1:
            print("Inside senior")
            senior_list = []
            seniors = SeniorCitizen.objects.filter(user = id)
            for senior in seniors:
                senior_list.append(senior.senior_citizen_id)
            final = Match.objects.filter(senior_citizen__in = senior_list).exclude(status="Pending")
        else:
            print("Inside parent")
            child_list = []
            pet_list = []
            childs = Child.objects.filter(user=id)
            child_serializer = ChildSerializer(childs, many=True)
            child_data = child_serializer.data
            for child in child_data:
                child_list.append(child['child_id'])
            child_matchs = Match.objects.filter(child__in=child_list).exclude(status="Pending")
            # pets = Pet.objects.filter(user=id)
            # for pet in pets:
            #     pet_list.append(pets.pet_id)
            # pet_matchs = Match.objects.filter(pet__in=pet_list).exclude(status="Pending")
            for child in child_matchs:
                final.add(child)
            # for pet in pet_matchs:
            #     final.add(pet)
        serializer = MatchSerializer(final, many=True)
        temp = serializer.data
        for one in temp:
            senior_name = SeniorCitizen.objects.get(senior_citizen_id=one['senior_citizen']).user.name
            child_name = Child.objects.get(child_id=one['child']).name
            if one["pet"] != None:
                pet_name = Pet.objects.get(pet_id=one['pet']).name
            else:
                pet_name = "No Pet"
            # print(senior_name,child_name, pet_name)
            newData = {"data": one,
                       "senior_name": senior_name,
                       "child_name": child_name,
                       "pet_name": pet_name}
            response_list.append(newData)
    return JsonResponse(response_list, safe=False)


@api_view(['GET','PUT'])
def match_details(request, id):
    if request.method == 'GET':
        match_details = Match.objects.filter(pet_id=id)
        serializer = MatchSerializer(match_details, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'PUT':
        queryset = Match.objects.all()
        update_data = get_object_or_404(queryset, match_id=id)
        serializer = MatchSerializer(update_data, data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
        return JsonResponse(serializer.data, safe=False)

@api_view(['POST'])
def add_match(request):
    if request.method == 'POST':
        serializer = MatchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def get_all_matchs(request):
    if request.method == 'GET':
        matchs = Match.objects.all()
        serializer = MatchSerializer(matchs, many=True)
        return JsonResponse(serializer.data, safe=False)

#--------------------------GET RECOMMENDATION-------------------------------------


@api_view(['GET'])
def get_recommendation_for_child(request,id):
    activity_pref_list = []
    recommended_senior_citizens = set()
    if request.method == 'GET':
        activity_prefs = Child.objects.get(child_id=id).activity_pref.all()
        for activ in activity_prefs:
            activity_pref_list.append(activ.activity_id)
        senior_citizens_activity = SeniorCitizen.objects.filter(activity_pref__in = activity_pref_list)
        zip_code = Child.objects.get(child_id=id).user.zip_code
        # print("ZIPCODE", zip_code)
        zcdb = ZipCodeDatabase()
        zip_list = [z.zip for z in zcdb.get_zipcodes_around_radius(zip_code, 5)]
        # print(zip_list)
        senior_citizens_zip = SeniorCitizen.objects.filter(user__zip_code__in=zip_list)
        # serializer = SeniorCitizenSerializer(senior_citizens_zip, many=True)
        #
        # print("ACTIVITY : ", senior_citizens_activity)
        # print("ZIP : ", senior_citizens_zip)
        count = 0
        size_activity = len(senior_citizens_activity)
        size_zip = len(senior_citizens_zip)
        act = 0
        zip = 0
        recom_final = []
        while count<3 :
            if count%2 == 0 :
                if act < size_activity and size_activity != 0:
                    recommended_senior_citizens.add(senior_citizens_activity[act])
                    act = act +1
                    count = len(recommended_senior_citizens)
                elif zip < size_zip and size_zip != 0:
                    recommended_senior_citizens.add(senior_citizens_zip[zip])
                    zip = zip+1
                    count = len(recommended_senior_citizens)
                else:
                    break
            elif count%2 !=0 :
                if zip < size_zip and size_zip != 0:
                    recommended_senior_citizens.add(senior_citizens_zip[zip])
                    zip = zip + 1
                    count = len(recommended_senior_citizens)
                elif act < size_activity and size_activity != 0:
                    recommended_senior_citizens.add(senior_citizens_activity[act])
                    act = act + 1
                    count = len(recommended_senior_citizens)
                else:
                    break

            print(recommended_senior_citizens)
            print("COUNT : ", count)

        serializer = SeniorCitizenSerializer(recommended_senior_citizens, many=True)

        temp = serializer.data
        for one in temp:
            activity_name = []
            activity_prefs = one['activity_pref']
            # print("ACTIVITIES ARE :",activity_prefs)
            for activ in activity_prefs:
                name = Activity.objects.get(activity_id=activ).name
                activity_name.append(name)
            one['activity_pref'] = activity_name


        return JsonResponse(temp,safe=False)



@api_view(['GET'])
def get_recommendation_for_child_activity(request,id):
    activity_pref_list = []
    recommended_senior_citizens = set()
    if request.method == 'GET':
        activity_prefs = Child.objects.get(child_id=id).activity_pref.all()
        for activ in activity_prefs:
            activity_pref_list.append(activ.activity_id)
        # print(activity_pref_list)
        # Blog.objects.filter(pk__in=[1, 4, 7])
        senior_citizens = SeniorCitizen.objects.filter(activity_pref__in = activity_pref_list)
        for obj in senior_citizens:
            recommended_senior_citizens.add(obj)
            if len(recommended_senior_citizens) == 3:
                break
        # print(recommended_senior_citizens)
        serializer = SeniorCitizenSerializer(recommended_senior_citizens, many=True)
        return JsonResponse(serializer.data, safe=False)



@api_view(['GET'])
def get_recommendation_for_pet_activity(request,id):
    activity_pref_list = []
    recommended_senior_citizens = set()
    if request.method == 'GET':
        activity_prefs = Pet.objects.get(pet_id=id).activity_pref.all()
        for activ in activity_prefs:
            activity_pref_list.append(activ.activity_id)
        senior_citizens = SeniorCitizen.objects.filter(activity_pref__in = activity_pref_list)
        for obj in senior_citizens:
            recommended_senior_citizens.add(obj)
            if len(recommended_senior_citizens) == 3:
                break
        serializer = SeniorCitizenSerializer(recommended_senior_citizens, many=True)
        return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def get_recommendation_for_senior_citizen_activity(request,id):
    activity_pref_list = []
    recommended_child = set()
    if request.method == 'GET':
        activity_prefs = SeniorCitizen.objects.get(senior_citizen_id=id).activity_pref.all()
        for activ in activity_prefs:
            activity_pref_list.append(activ.activity_id)
        senior_citizens = Child.objects.filter(activity_pref__in = activity_pref_list)
        for obj in senior_citizens:
            recommended_child.add(obj)
            if len(recommended_child) == 3:
                break
        serializer = ChildSerializer(recommended_child, many=True)
        return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def get_recommendation_for_senior(request,id):
    activity_pref_list = []
    recommended_child = set()
    if request.method == 'GET':
        activity_prefs = SeniorCitizen.objects.get(senior_citizen_id=id).activity_pref.all()
        for activ in activity_prefs:
            activity_pref_list.append(activ.activity_id)
        child_activity = Child.objects.filter(activity_pref__in = activity_pref_list)
        zip_code = SeniorCitizen.objects.get(senior_citizen_id=id).user.zip_code
        # print("ZIPCODE", zip_code)
        zcdb = ZipCodeDatabase()
        zip_list = [z.zip for z in zcdb.get_zipcodes_around_radius(zip_code, 5)]
        # print(zip_list)
        child_zip = Child.objects.filter(user__zip_code__in=zip_list)
        # serializer = SeniorCitizenSerializer(senior_citizens_zip, many=True)
        #
        # print("ACTIVITY : ", senior_citizens_activity)
        # print("ZIP : ", senior_citizens_zip)
        count = 0
        size_activity = len(child_activity)
        size_zip = len(child_zip)
        act = 0
        zip = 0
        recom_final = []
        while count<3 :
            if count%2 == 0 :
                if act < size_activity and size_activity != 0:
                    recommended_child.add(child_activity[act])
                    act = act +1
                    count = len(recommended_child)
                elif zip < size_zip and size_zip != 0:
                    recommended_child.add(child_zip[zip])
                    zip = zip+1
                    count = len(recommended_child)
                else:
                    break
            elif count%2 !=0 :
                if zip < size_zip and size_zip != 0:
                    recommended_child.add(child_zip[zip])
                    zip = zip + 1
                    count = len(recommended_child)
                elif act < size_activity and size_activity != 0:
                    recommended_child.add(child_activity[act])
                    act = act + 1
                    count = len(recommended_child)
                else:
                    break

            # print(recommended_child)
            # print("COUNT : ", count)

        serializer = ChildSerializer(recommended_child, many=True)

        temp = serializer.data
        for one in temp:
            activity_name = []
            activity_prefs = one['activity_pref']
            # print("ACTIVITIES ARE :",activity_prefs)
            for activ in activity_prefs:
                name = Activity.objects.get(activity_id=activ).name
                activity_name.append(name)
            one['activity_pref'] = activity_name

        return JsonResponse(temp, safe=False)

#LOCATION
@api_view(['GET'])
def get_recommendation_for_child_location(request,id):
    if request.method == 'GET':
        zip_code = Child.objects.get(child_id=id).user.zip_code
        print(zip_code)
        zcdb = ZipCodeDatabase()
        zip_list = [z.zip for z in zcdb.get_zipcodes_around_radius(zip_code, 5)]
        senior_citizens = SeniorCitizen.objects.filter(user__zip_code__in = zip_list)
        serializer = SeniorCitizenSerializer(senior_citizens, many=True)
        return JsonResponse(serializer.data, safe=False)

#
#
# @api_view(['GET'])
# def get_recommendation_for_pet_location(request,id):
#     activity_pref_list = []
#     recommended_senior_citizens = set()
#     if request.method == 'GET':
#         activity_prefs = Pet.objects.get(pet_id=id).activity_pref.all()
#         for activ in activity_prefs:
#             activity_pref_list.append(activ.activity_id)
#         senior_citizens = SeniorCitizen.objects.filter(activity_pref__in = activity_pref_list)
#         for obj in senior_citizens:
#             recommended_senior_citizens.add(obj)
#             if len(recommended_senior_citizens) == 3:
#                 break
#         serializer = SeniorCitizenSerializer(recommended_senior_citizens, many=True)
#         return JsonResponse(serializer.data, safe=False)
#
# @api_view(['GET'])
# def get_recommendation_for_senior_citizen_location(request,id):
#     activity_pref_list = []
#     recommended_child = set()
#     if request.method == 'GET':
#         activity_prefs = SeniorCitizen.objects.get(senior_citizen_id=id).activity_pref.all()
#         for activ in activity_prefs:
#             activity_pref_list.append(activ.activity_id)
#         senior_citizens = Child.objects.filter(activity_pref__in = activity_pref_list)
#         for obj in senior_citizens:
#             recommended_child.add(obj)
#             if len(recommended_child) == 3:
#                 break
#         serializer = ChildSerializer(recommended_child, many=True)
#         return JsonResponse(serializer.data, safe=False)
#
#

#-----------------------------------------------------------------------------------------------------------------------------------

@api_view(['GET'])
def getData(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


# @api_view(['POST'])
# def addUser(request):
#     serializer = UserSerializer(data=request.data )
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)
# usertype = UserType.objects.filter(user_type_id=id)
 # usertype = UserType.objects.filter(user_type_id=id)
    # serializer = UserTypeSerializer(users, many=True)
