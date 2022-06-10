from datetime import date
import itertools
import threading
import time
import sys

#For ID Registration-------------
students_id = list(range(1000000))
num_of_stud = len(students_id)

class election():

    #Candidates for President----------------------------------
    p1_no = 1
    p2_no = 2
    p3_no = 3
    p1_name = "Salman Rehman from BS Info. Tech. 2C"
    p2_name = "Roman Khan from BS Info. Tech. 2C"
    p3_name = "Faisal imran from BS Info. Tech. 2C"
    pres_1 = 0
    pres_2 = 0
    pres_3 = 0
    # Candidates for Vice President----------------------------------
    vp1_no = 1
    vp2_no = 2
    vp3_no = 3
    vp1_name = "Tanveer faisal from BS Info. Tech. 2C"
    vp2_name = "Inam Khan from BS Info. Tech. 2C"
    vp3_name = "Talha Arshad from BS Info. Tech. 2C"
    vpres_1 = 0
    vpres_2 = 0
    vpres_3 = 0
    # Candidates for Secretary----------------------------------
    sec1_no = 1
    sec2_no = 2
    sec3_no = 3
    sec1_name = "Hikmat ullah from BS Info. Tech. 2C"
    sec2_name = "Afaq Khan from BS Info. Tech. 2C"
    sec3_name = "Sikandar shah from BS Info. Tech. 2C"
    sec_1 = 0
    sec_2 = 0
    sec_3 = 0
    # Candidates for Auditor----------------------------------
    aud1_no = 1
    aud2_no = 2
    aud3_no = 3
    aud1_name = "Rafi Ullah from BS Info. Tech. 2C"
    aud2_name = "Bilal Khan Tuando from BS Info. Tech. 2C"
    aud3_name = "Abubakar Belleza from BS Info. Tech. 2C"
    aud_1 = 0
    aud_2 = 0
    aud_3 = 0
    # Candidates for Treasurer----------------------------------
    tre1_no = 1
    tre2_no = 2
    tre3_no = 3
    tre1_name = "Asad Khan from BS Info. Tech. 2C"
    tre2_name = "Habib ullah from BS Info. Tech. 2C"
    tre3_name = "Sudais khan from BS Info. Tech. 2C"
    tre_1 = 0
    tre_2 = 0
    tre_3 = 0
    # Candidates for Media Information----------------------------------
    media1_no = 1
    media2_no = 2
    media3_no = 3
    media1_name = "karim khan from BS Info. Tech. 2C"
    media2_name = "Khalil ullah from BS Info. Tech. 2C"
    media3_name = "abdur rehman from BS Info. Tech. 2C"
    media_1 = 0
    media_2 = 0
    media_3 = 0
    # Candidates for First Year Representative----------------------------------
    f_rep1_no = 1
    f_rep2_no = 2
    f_rep3_no = 3
    f_rep1_name = "yusra from BS Info. Tech. 1A"
    f_rep2_name = "Taj mahal from BS Info. Tech. 1B"
    f_rep3_name = "Kashmala from BS Info. Tech. 1C"
    f_rep_1 = 0
    f_rep_2 = 0
    f_rep_3 = 0
    # Candidates for Second Year Representative----------------------------------
    s_rep1_no = 1
    s_rep2_no = 2
    s_rep3_no = 3
    s_rep1_name = "huzaifa from BS Info. Tech. 2A"
    s_rep2_name = "owais  from BS Info. Tech. 2B"
    s_rep3_name = "wasif  from BS Info. Tech. 2C"
    s_rep_1 = 0
    s_rep_2 = 0
    s_rep_3 = 0
    # Candidates for Third Year Representative----------------------------------
    t_rep1_no = 1
    t_rep2_no = 2
    t_rep3_no = 3
    t_rep1_name = "Rafi Ullah BS Info. Tech. 3A"
    t_rep2_name = "Asad aslam from BS Info. Tech. 3B"
    t_rep3_name = "Aatif khan from BS Info. Tech. 3C"
    t_rep_1 = 0
    t_rep_2 = 0
    t_rep_3 = 0
    # Candidates for Fourth Year Representative----------------------------------
    frt_rep1_no = 1
    frt_rep2_no = 2
    frt_rep3_no = 3
    frt_rep1_name = "azan  from BS Info. Tech. 4A"
    frt_rep2_name = "babar from BS Info. Tech. 4B"
    frt_rep3_name = "yaseen from BS Info. Tech. 4C"
    frt_rep_1 = 0
    frt_rep_2 = 0
    frt_rep_3 = 0

    def welcome(obj):
        today = date.today()
        datetime = today.strftime("%B %d, %Y")
        print("-----------------------------------------------------------------------")
        print("                 ERLCOME TO VOTING SYSTEM                  ")
        print("          UNIVERSITY OF SWAT BS DCST        ")
        print("                   PTCL CAMPUS - " + datetime + "                  ")
        print("-----------------------------------------------------------------------")
        print("************* Welcome to SSG Elections for 2021-2022 *************")

    def loading(obj):
        done = False

        # here is the animation
        def animate():
            for c in itertools.cycle(['|', '/', '-', '\\']):
                if done:
                    break
                sys.stdout.write('\rAnalyzing ID...' + c)
                sys.stdout.flush()
                time.sleep(0.1)

        t = threading.Thread(target=animate)
        t.start()

        # long process here
        time.sleep(2)
        done = True

    def error_loading(obj):
        done = False

        # here is the animation
        def animate():
            for c in itertools.cycle(['|', '/', '-', '\\']):
                if done:
                    break
                sys.stdout.write('\rAnalyzing ID...' + c)
                sys.stdout.flush()
                time.sleep(0.1)

        t = threading.Thread(target=animate)
        t.start()

        # long process here
        time.sleep(5)
        done = True

    def loading_result(obj):
        done = False

        # here is the animation
        def animate():
            for c in itertools.cycle(['|', '/', '-', '\\']):
                if done:
                    break
                sys.stdout.write('\rPlease wait while reading the result...' + c)
                sys.stdout.flush()
                time.sleep(0.1)

        t = threading.Thread(target=animate)
        t.start()

        # long process here
        time.sleep(8)
        done = True

    def registration(obj):

        while True:
            print("-----------------------------REGISTRATION-----------------------------")
            print("")
            obj.f_name = input("First name: ")
            obj.l_name = input("Last name: ")
            obj.course = input("BS in: ")
            obj.year_section = input("Year & section: ")
            obj.stud_id = int(input("Student ID no.: "))
            if obj.stud_id in students_id:
                students_id.remove(obj.stud_id)
                obj.loading()
                print("Done!")
                print('-----------------------Registered Successfully!-----------------------')
                print("Name: " + obj.f_name + " " + obj.l_name)
                print("Course: Bachelor of Science in " + obj.course)
                print("Year & Section: " + obj.year_section)
                print("Voter's ID: " + str(obj.stud_id))
                obj.president()
                obj.vice_pres()
                obj.secretary()
                obj.auditor()
                obj.treasurer()
                obj.media_info()
                obj.first_yr_rep()
                obj.sec_yr_rep()
                obj.third_yr_rep()
                obj.fourth_yr_rep()
                break
            else:
                obj.error_loading()
                print("Done!")
                print("------------------ID existed. You have already voted!----------------")
                print("---------------------------PLEASE TRY AGAIN--------------------------\n")

#President --------------------------------------------------------
    def president(obj):

        print("----------------------------------------------------------------------")
        proceed_pres = int(input("Do you want to proceed voting in President? 1. Yes / 2. No : "))
        if proceed_pres == 1:
            pres = 1
            while pres <= float('inf'):
                print("----------------------------------------------------------------------")
                print("The candidtates running for President are: \n")
                print(str(obj.p1_no) + ") " + obj.p1_name)
                print(str(obj.p2_no) + ") " + obj.p2_name)
                print(str(obj.p3_no) + ") " + obj.p3_name)
                print("----------------------------------------------------------------------")
                pres_vote = int(input("Press the number of candidate you want to vote for: "))
                if pres_vote == 1:
                    obj.pres_1 += 1
                    pres1_final = obj.p1_name + " = " + str(obj.pres_1)
                    print("----------------------------------------------------------------------")
                    print("Total votes for " + str(pres1_final))
                    print("Total votes for " + obj.p2_name + " = " + str(obj.pres_2))
                    print("Total votes for " + obj.p3_name + " = " + str(obj.pres_3))
                    obj.vice_pres()
                    break
                elif pres_vote == 2:
                    obj.pres_2 += 1
                    pres2_final = obj.p2_name + " = " + str(obj.pres_2)
                    print("----------------------------------------------------------------------")
                    print("Total votes for " + obj.p1_name + " = " + str(obj.pres_1))
                    print("Total votes for " + str(pres2_final))
                    print("Total votes for " + obj.p3_name + " = " + str(obj.pres_3))
                    obj.vice_pres()
                    break
                elif pres_vote == 3:
                    obj.pres_3 += 1
                    pres3_final = obj.p3_name + " = " + str(obj.pres_3)
                    print("----------------------------------------------------------------------")
                    print("Total votes for " + obj.p1_name + " = " + str(obj.pres_1))
                    print("Total votes for " + obj.p2_name + " = " + str(obj.pres_2))
                    print("Total votes for " + str(pres3_final))
                    obj.vice_pres()
                    break
                else:
                    print("Invalid input. Please try again.")
                    print("----------------------------------------------------------------------")
        elif proceed_pres == 2:
            obj.vice_pres()
        else:
            print("Invalid input. Please try again.")
            print("----------------------------------------------------------------------")

#Vice president --------------------------------------------------------

    def vice_pres(obj):

        print("----------------------------------------------------------------------")
        proceed_vpres = int(input("Do you want to proceed voting in Vice President? 1. Yes / 2. No : "))
        if proceed_vpres == 1:
            vpres = 1
            while vpres <= float('inf'):
                print("----------------------------------------------------------------------")
                print("The candidtates running for Vice President are: \n")
                print(str(obj.vp1_no) + ") " + obj.vp1_name)
                print(str(obj.vp2_no) + ") " + obj.vp2_name)
                print(str(obj.vp3_no) + ") " + obj.vp3_name)
                print("----------------------------------------------------------------------")
                vpres_vote = int(input("Press the number of candidate you want to vote for: "))
                if vpres_vote == 1:
                    obj.vpres_1 += 1
                    vpres1_final = obj.vp1_name + " = " + str(obj.vpres_1)
                    print("----------------------------------------------------------------------")
                    print("Total votes for " + str(vpres1_final))
                    print("Total votes for " + obj.vp2_name + " = " + str(obj.vpres_2))
                    print("Total votes for " + obj.vp3_name + " = " + str(obj.vpres_3))
                    obj.secretary()
                    break
                elif vpres_vote == 2:
                    obj.vpres_2 += 1
                    vpres2_final = obj.vp2_name + " = " + str(obj.vpres_2)
                    print("----------------------------------------------------------------------")
                    print("Total votes for " + obj.vp1_name + " = " + str(obj.vpres_1))
                    print("Total votes for " + str(vpres2_final))
                    print("Total votes for " + obj.vp3_name + " = " + str(obj.vpres_3))
                    obj.secretary()
                    break
                elif vpres_vote == 3:
                    obj.vpres_3 += 1
                    vpres3_final = obj.vp3_name + " = " + str(obj.vpres_3)
                    print("----------------------------------------------------------------------")
                    print("Total votes for " + obj.vp1_name + " = " + str(obj.vpres_1))
                    print("Total votes for " + obj.vp2_name + " = " + str(obj.vpres_2))
                    print("Total votes for " + str(vpres3_final))
                    obj.secretary()
                    break
                else:
                    print("Invalid input. Please try again.")
        elif proceed_vpres == 2:
            obj.secretary()
        else:
            print("Invalid input. Please try again.")

#Secretary --------------------------------------------------------

    def secretary(obj):

        print("----------------------------------------------------------------------")
        proceed_sec = int(input("Do you want to proceed voting in Secretary? 1. Yes / 2. No : "))
        if proceed_sec == 1:
            sec = 1
            while sec <= float('inf'):
                print("----------------------------------------------------------------------")
                print("The candidtates running for Secretary are: \n")
                print(str(obj.sec1_no) + ") " + obj.sec1_name)
                print(str(obj.sec2_no) + ") " + obj.sec2_name)
                print(str(obj.sec3_no) + ") " + obj.sec3_name)
                print("----------------------------------------------------------------------")
                sec_vote = int(input("Press the number of candidate you want to vote for: "))
                if sec_vote == 1:
                    obj.sec_1 += 1
                    sec_final = obj.sec1_name + " = " + str(obj.sec_1)
                    print("----------------------------------------------------------------------")
                    print("Total votes for " + str(sec_final))
                    print("Total votes for " + obj.sec2_name + " = " + str(obj.sec_2))
                    print("Total votes for " + obj.sec3_name + " = " + str(obj.sec_3))
                    obj.auditor()
                    break
                elif sec_vote == 2:
                    obj.sec_2 += 1
                    sec2_final = obj.sec2_name + " = " + str(obj.sec_2)
                    print("----------------------------------------------------------------------")
                    print("Total votes for " + obj.sec1_name + " = " + str(obj.sec_1))
                    print("Total votes for " + str(sec2_final))
                    print("Total votes for " + obj.sec3_name + " = " + str(obj.sec_3))
                    obj.auditor()
                    break
                elif sec_vote == 3:
                    obj.sec_3 += 1
                    sec3_final = obj.sec3_name + " = " + str(obj.sec_3)
                    print("----------------------------------------------------------------------")
                    print("Total votes for " + obj.sec1_name + " = " + str(obj.sec_1))
                    print("Total votes for " + obj.sec2_name + " = " + str(obj.sec_2))
                    print("Total votes for " + str(sec3_final))
                    obj.auditor()
                    break
                else:
                    print("Invalid input. Please try again.")
        elif proceed_sec == 2:
            obj.auditor()
        else:
            print("Invalid input. Please try again.")

#Auditor --------------------------------------------------------

    def auditor(obj):

        print("----------------------------------------------------------------------")
        proceed_aud = int(input("Do you want to proceed voting in Auditor? 1. Yes / 2. No : "))
        if proceed_aud == 1:
            aud = 1
            while aud <= float('inf'):
                print("----------------------------------------------------------------------")
                print("The candidtates running for Auditor are: \n")
                print(str(obj.aud1_no) + ") " + obj.aud1_name)
                print(str(obj.aud2_no) + ") " + obj.aud2_name)
                print(str(obj.aud3_no) + ") " + obj.aud3_name)
                print("----------------------------------------------------------------------")
                aud_vote = int(input("Press the number of candidate you want to vote for: "))
                if aud_vote == 1:
                    obj.aud_1 += 1
                    aud_final = obj.aud1_name + " = " + str(obj.aud_1)
                    print("----------------------------------------------------------------------")
                    print("Total votes for " + str(aud_final))
                    print("Total votes for " + obj.aud2_name + " = " + str(obj.aud_2))
                    print("Total votes for " + obj.aud3_name + " = " + str(obj.aud_3))
                    obj.treasurer()
                    break
                elif aud_vote == 2:
                    obj.aud_2 += 1
                    aud2_final = obj.aud2_name + " = " + str(obj.aud_2)
                    print("----------------------------------------------------------------------")
                    print("Total votes for " + obj.aud1_name + " = " + str(obj.aud_1))
                    print("Total votes for " + str(aud2_final))
                    print("Total votes for " + obj.aud3_name + " = " + str(obj.aud_3))
                    obj.treasurer()
                    break
                elif aud_vote == 3:
                    obj.aud_3 += 1
                    aud3_final = obj.aud3_name + " = " + str(obj.aud_3)
                    print("----------------------------------------------------------------------")
                    print("Total votes for " + obj.aud1_name + " = " + str(obj.aud_1))
                    print("Total votes for " + obj.aud2_name + " = " + str(obj.aud_2))
                    print("Total votes for " + str(aud3_final))
                    obj.treasurer()
                    break
                else:
                    print("Invalid input. Please try again.")
        elif proceed_aud == 2:
            obj.treasurer()
        else:
            print("Invalid input. Please try again.")

#Treasurer --------------------------------------------------------

    def treasurer(obj):

        print("----------------------------------------------------------------------")
        proceed_tre = int(input("Do you want to proceed voting in Treasurer? 1. Yes / 2. No : "))
        if proceed_tre == 1:
            tre = 1
            while tre <= float('inf'):
                print("----------------------------------------------------------------------")
                print("The candidtates running for Treasurer are: \n")
                print(str(obj.tre1_no) + ") " + obj.tre1_name)
                print(str(obj.tre2_no) + ") " + obj.aud2_name)
                print(str(obj.tre3_no) + ") " + obj.tre3_name)
                print("----------------------------------------------------------------------")
                tre_vote = int(input("Press the number of candidate you want to vote for: "))
                if tre_vote == 1:
                    obj.tre_1 += 1
                    tre_final = obj.tre1_name + " = " + str(obj.tre_1)
                    print("----------------------------------------------------------------------")
                    print("Total votes for " + str(tre_final))
                    print("Total votes for " + obj.tre2_name + " = " + str(obj.tre_2))
                    print("Total votes for " + obj.tre3_name + " = " + str(obj.tre_3))
                    obj.media_info()
                    break
                elif tre_vote == 2:
                    obj.tre_2 += 1
                    tre2_final = obj.tre2_name + " = " + str(obj.tre_2)
                    print("----------------------------------------------------------------------")
                    print("Total votes for " + obj.tre1_name + " = " + str(obj.tre_1))
                    print("Total votes for " + str(tre2_final))
                    print("Total votes for " + obj.tre3_name + " = " + str(obj.tre_3))
                    obj.media_info()
                    break
                elif tre_vote == 3:
                    obj.tre_3 += 1
                    tre3_final = obj.tre3_name + " = " + str(obj.tre_3)
                    print("----------------------------------------------------------------------")
                    print("Total votes for " + obj.tre1_name + " = " + str(obj.tre_1))
                    print("Total votes for " + obj.tre2_name + " = " + str(obj.tre_2))
                    print("Total votes for " + str(tre3_final))
                    obj.media_info()
                    break
                else:
                    print("Invalid input. Please try again.")
        elif proceed_tre == 2:
            obj.media_info()
        else:
            print("Invalid input. Please try again.")

#Media Information --------------------------------------------------------

    def media_info(obj):

        print("----------------------------------------------------------------------")
        proceed_media = int(input("Do you want to proceed voting in Media Information? 1. Yes / 2. No : "))
        if proceed_media == 1:
            media = 1
            while media <= float('inf'):
                print("----------------------------------------------------------------------")
                print("The candidtates running for Media Information are: \n")
                print(str(obj.media1_no) + ") " + obj.media1_name)
                print(str(obj.media2_no) + ") " + obj.media2_name)
                print(str(obj.media3_no) + ") " + obj.media3_name)
                print("----------------------------------------------------------------------")
                media_vote = int(input("Press the number of candidate you want to vote for: "))
                if media_vote == 1:
                    obj.media_1 += 1
                    media_final = obj.media1_name + " = " + str(obj.media_1)
                    print("----------------------------------------------------------------------")
                    print("Total votes for " + str(media_final))
                    print("Total votes for " + obj.media2_name + " = " + str(obj.media_2))
                    print("Total votes for " + obj.media3_name + " = " + str(obj.media_3))
                    obj.first_yr_rep()
                    break
                elif media_vote == 2:
                    obj.media_2 += 1
                    media2_final = obj.media2_name + " = " + str(obj.media_2)
                    print("----------------------------------------------------------------------")
                    print("Total votes for " + obj.media1_name + " = " + str(obj.media_1))
                    print("Total votes for " + str(media2_final))
                    print("Total votes for " + obj.media3_name + " = " + str(obj.media_3))
                    obj.first_yr_rep()
                    break
                elif media_vote == 3:
                    obj.media_3 += 1
                    media3_final = obj.media3_name + " = " + str(obj.media_3)
                    print("----------------------------------------------------------------------")
                    print("Total votes for " + obj.media1_name + " = " + str(obj.media_1))
                    print("Total votes for " + obj.media2_name + " = " + str(obj.media_2))
                    print("Total votes for " + str(media3_final))
                    obj.first_yr_rep()
                    break
                else:
                    print("Invalid input. Please try again.")
        elif proceed_media == 2:
            obj.first_yr_rep()
        else:
            print("Invalid input. Please try again.")

#First Year Representatives --------------------------------------------------------

    def first_yr_rep(obj):

        print("----------------------------------------------------------------------")
        proceed_f_rep = int(input("Do you want to proceed voting in First Year Representative? 1. Yes / 2. No : "))
        if proceed_f_rep == 1:
            f_rep = 1
            while f_rep <= float('inf'):
                print("----------------------------------------------------------------------")
                print("The candidtates running for First Year Representative are: \n")
                print(str(obj.f_rep1_no) + ") " + obj.f_rep1_name)
                print(str(obj.f_rep2_no) + ") " + obj.f_rep2_name)
                print(str(obj.f_rep3_no) + ") " + obj.f_rep3_name)
                print("----------------------------------------------------------------------")
                f_rep_vote = int(input("Press the number of candidate you want to vote for: "))
                if f_rep_vote == 1:
                    obj.f_rep_1 += 1
                    f_rep_final = obj.f_rep1_name + " = " + str(obj.f_rep_1)
                    print("----------------------------------------------------------------------")
                    print("Total votes for " + str(f_rep_final))
                    print("Total votes for " + obj.f_rep2_name + " = " + str(obj.f_rep_2))
                    print("Total votes for " + obj.f_rep3_name + " = " + str(obj.f_rep_3))
                    obj.sec_yr_rep()
                    break
                elif f_rep_vote == 2:
                    obj.f_rep_2 += 1
                    f_rep2_final = obj.f_rep2_name + " = " + str(obj.f_rep_2)
                    print("----------------------------------------------------------------------")
                    print("Total votes for " + obj.f_rep1_name + " = " + str(obj.f_rep_1))
                    print("Total votes for " + str(f_rep2_final))
                    print("Total votes for " + obj.f_rep3_name + " = " + str(obj.f_rep_3))
                    obj.sec_yr_rep()
                    break
                elif f_rep_vote == 3:
                    obj.f_rep_3 += 1
                    f_rep3_final = obj.f_rep3_name + " = " + str(obj.f_rep_3)
                    print("----------------------------------------------------------------------")
                    print("Total votes for " + obj.f_rep1_name + " = " + str(obj.f_rep_1))
                    print("Total votes for " + obj.f_rep2_name + " = " + str(obj.f_rep_2))
                    print("Total votes for " + str(f_rep3_final))
                    obj.sec_yr_rep()
                    break
                else:
                    print("Invalid input. Please try again.")
        elif proceed_f_rep == 2:
            obj.sec_yr_rep()
        else:
            print("Invalid input. Please try again.")

#Second Year Representatives --------------------------------------------------------

    def sec_yr_rep(obj):

        print("----------------------------------------------------------------------")
        proceed_s_rep = int(input("Do you want to proceed voting in Second Year Representative? 1. Yes / 2. No : "))
        if proceed_s_rep == 1:
            s_rep = 1
            while s_rep <= float('inf'):
                print("----------------------------------------------------------------------")
                print("The candidtates running for Second Year Representative are: \n")
                print(str(obj.s_rep1_no) + ") " + obj.s_rep1_name)
                print(str(obj.s_rep2_no) + ") " + obj.s_rep2_name)
                print(str(obj.s_rep3_no) + ") " + obj.s_rep3_name)
                print("----------------------------------------------------------------------")
                s_rep_vote = int(input("Press the number of candidate you want to vote for: "))
                if s_rep_vote == 1:
                    obj.s_rep_1 += 1
                    s_rep_final = obj.s_rep1_name + " = " + str(obj.s_rep_1)
                    print("----------------------------------------------------------------------")
                    print("Total votes for " + str(s_rep_final))
                    print("Total votes for " + obj.s_rep2_name + " = " + str(obj.s_rep_2))
                    print("Total votes for " + obj.s_rep3_name + " = " + str(obj.s_rep_3))
                    obj.third_yr_rep()
                    break
                elif s_rep_vote == 2:
                    obj.s_rep_2 += 1
                    s_rep2_final = obj.s_rep2_name + " = " + str(obj.s_rep_2)
                    print("----------------------------------------------------------------------")
                    print("Total votes for " + obj.s_rep1_name + " = " + str(obj.s_rep_1))
                    print("Total votes for " + str(s_rep2_final))
                    print("Total votes for " + obj.s_rep3_name + " = " + str(obj.s_rep_3))
                    obj.third_yr_rep()
                    break
                elif s_rep_vote == 3:
                    obj.s_rep_3 += 1
                    s_rep3_final = obj.s_rep3_name + " = " + str(obj.s_rep_3)
                    print("----------------------------------------------------------------------")
                    print("Total votes for " + obj.s_rep1_name + " = " + str(obj.s_rep_1))
                    print("Total votes for " + obj.s_rep2_name + " = " + str(obj.s_rep_2))
                    print("Total votes for " + str(s_rep3_final))
                    obj.third_yr_rep()
                    break
                else:
                    print("Invalid input. Please try again.")
        elif proceed_s_rep == 2:
            obj.third_yr_rep()
        else:
            print("Invalid input. Please try again.")

#Third Year Representatives --------------------------------------------------------

    def third_yr_rep(obj):

        print("----------------------------------------------------------------------")
        proceed_t_rep = int(input("Do you want to proceed voting in Third Year Representative? 1. Yes / 2. No : "))
        if proceed_t_rep == 1:
            t_rep = 1
            while t_rep <= float('inf'):
                print("----------------------------------------------------------------------")
                print("The candidtates running for Third Year Representative are: \n")
                print(str(obj.t_rep1_no) + ") " + obj.t_rep1_name)
                print(str(obj.t_rep2_no) + ") " + obj.t_rep2_name)
                print(str(obj.t_rep3_no) + ") " + obj.t_rep3_name)
                print("----------------------------------------------------------------------")
                t_rep_vote = int(input("Press the number of candidate you want to vote for: "))
                if t_rep_vote == 1:
                    obj.t_rep_1 += 1
                    t_rep_final = obj.t_rep1_name + " = " + str(obj.t_rep_1)
                    print("----------------------------------------------------------------------")
                    print("Total votes for " + str(t_rep_final))
                    print("Total votes for " + obj.t_rep2_name + " = " + str(obj.t_rep_2))
                    print("Total votes for " + obj.t_rep3_name + " = " + str(obj.t_rep_3))
                    obj.fourth_yr_rep()
                    break
                elif t_rep_vote == 2:
                    obj.t_rep_2 += 1
                    t_rep2_final = obj.t_rep2_name + " = " + str(obj.t_rep_2)
                    print("----------------------------------------------------------------------")
                    print("Total votes for " + obj.t_rep1_name + " = " + str(obj.t_rep_1))
                    print("Total votes for " + str(t_rep2_final))
                    print("Total votes for " + obj.t_rep3_name + " = " + str(obj.t_rep_3))
                    obj.fourth_yr_rep()
                    break
                elif t_rep_vote == 3:
                    obj.t_rep_3 += 1
                    t_rep3_final = obj.t_rep3_name + " = " + str(obj.t_rep_3)
                    print("----------------------------------------------------------------------")
                    print("Total votes for " + obj.t_rep1_name + " = " + str(obj.t_rep_1))
                    print("Total votes for " + obj.t_rep2_name + " = " + str(obj.t_rep_2))
                    print("Total votes for " + str(t_rep3_final))
                    obj.fourth_yr_rep()
                    break
                else:
                    print("Invalid input. Please try again.")
        elif proceed_t_rep == 2:
            obj.fourth_yr_rep()
        else:
            print("Invalid input. Please try again.")

#Fourth Year Representatives --------------------------------------------------------

    def fourth_yr_rep(obj):

        print("----------------------------------------------------------------------")
        proceed_frt_rep = int(input("Do you want to proceed voting in Fourth Year Representative? 1. Yes / 2. No : "))
        if proceed_frt_rep == 1:
            frt_rep = 1
            while frt_rep <= float('inf'):
                print("----------------------------------------------------------------------")
                print("The candidtates running for Fourth Year Representative are: \n")
                print(str(obj.frt_rep1_no) + ") " + obj.frt_rep1_name)
                print(str(obj.frt_rep2_no) + ") " + obj.frt_rep2_name)
                print(str(obj.frt_rep3_no) + ") " + obj.frt_rep3_name)
                print("----------------------------------------------------------------------")
                frt_rep_vote = int(input("Press the number of candidate you want to vote for: "))
                if frt_rep_vote == 1:
                    obj.frt_rep_1 += 1
                    frt_rep_final = obj.frt_rep1_name + " = " + str(obj.frt_rep_1)
                    print("----------------------------------------------------------------------")
                    print("Total votes for " + str(frt_rep_final))
                    print("Total votes for " + obj.frt_rep2_name + " = " + str(obj.frt_rep_2))
                    print("Total votes for " + obj.frt_rep3_name + " = " + str(obj.frt_rep_3))
                    obj.another_vote()
                    break
                elif frt_rep_vote == 2:
                    obj.frt_rep_2 += 1
                    frt_rep2_final = obj.frt_rep2_name + " = " + str(obj.frt_rep_2)
                    print("----------------------------------------------------------------------")
                    print("Total votes for " + obj.frt_rep1_name + " = " + str(obj.frt_rep_1))
                    print("Total votes for " + str(frt_rep2_final))
                    print("Total votes for " + obj.frt_rep3_name + " = " + str(obj.frt_rep_3))
                    obj.another_vote()
                    break
                elif frt_rep_vote == 3:
                    obj.frt_rep_3 += 1
                    frt_rep3_final = obj.frt_rep3_name + " = " + str(obj.frt_rep_3)
                    print("----------------------------------------------------------------------")
                    print("Total votes for " + obj.frt_rep1_name + " = " + str(obj.frt_rep_1))
                    print("Total votes for " + obj.frt_rep2_name + " = " + str(obj.frt_rep_2))
                    print("Total votes for " + str(frt_rep3_final))
                    obj.another_vote()
                    break
                else:
                    print("Invalid input. Please try again.")
        elif proceed_frt_rep == 2:
            obj.another_vote()
        else:
            print("Invalid input. Please try again.")

#Another vote --------------------------------------------------------

    def another_vote(obj):
        a = """  IF ANY OF THE POSITION GOT A TIE VOTE RESULTS, JUST START THE PROGRAM OVER AGAIN
AND KINDLY SKIP (DO NOT PROCEED) TO THE POSITION THAT DOES NOT HAVE A TIE VOTE RESULT"""
        print("----------------------------------------------------------------------")
        an_vote = int(input("DO YOU WANT TO PROCEED ANOTHER VOTE? 1. Yes / 2. No : "))
        while True:
            if an_vote == 1:
                obj.registration()
                obj.president()
                obj.vice_pres()
                obj.secretary()
                obj.auditor()
                obj.treasurer()
                obj.media_info()
                obj.first_yr_rep()
                obj.sec_yr_rep()
                obj.third_yr_rep()
                obj.fourth_yr_rep()
                break
            elif an_vote == 2:
                obj.loading_result()
                obj.result()
                print(a)
                sys.exit()
            else:
                print("Invalid input. Please try again.")

#Results --------------------------------------------------------

    def result(obj):
        #Ranking for President----------------------------
        pres_total = (obj.pres_1, obj.pres_2, obj.pres_3)
        pres_result = max(pres_total)
        # Ranking for Vice President----------------------------
        vp_total = (obj.vpres_1, obj.vpres_2, obj.vpres_3)
        vp_result = max(vp_total)
        # Ranking for Secretary----------------------------
        sec_total = (obj.sec_1, obj.sec_2, obj.sec_3)
        sec_result = max(sec_total)
        # Ranking for Auditor----------------------------
        aud_total = (obj.aud_1, obj.aud_2, obj.aud_3)
        aud_result = max(aud_total)
        # Ranking for Treasurer----------------------------
        tre_total = (obj.tre_1, obj.tre_2, obj.tre_3)
        tre_result = max(tre_total)
        # Ranking for Media Information----------------------------
        media_total = (obj.media_1, obj.media_2, obj.media_3)
        media_result = max(media_total)
        # Ranking for First Year Representative----------------------------
        f_rep_total = (obj.f_rep_1, obj.f_rep_2, obj.f_rep_3)
        f_rep_result = max(f_rep_total)
        # Ranking for Second Year Representative----------------------------
        s_rep_total = (obj.s_rep_1, obj.s_rep_2, obj.s_rep_3)
        s_rep_result = max(s_rep_total)
        # Ranking for Third Year Representative----------------------------
        t_rep_total = (obj.t_rep_1, obj.t_rep_2, obj.t_rep_3)
        t_rep_result = max(t_rep_total)
        # Ranking for Fourth Year Representative----------------------------
        frt_rep_total = (obj.frt_rep_1, obj.frt_rep_2, obj.frt_rep_3)
        frt_rep_result = max(frt_rep_total)
        print("")
        print("***************** SUPREME STUDENT GOVERNMENT S.Y. 2021-2022 ******************")
        print("")
        # Final Result for President ------------------------------------------------------------------------
        if ((obj.pres_1 > obj.pres_2) and (obj.pres_1 > obj.pres_3)):
            print("****************** New elected President for S.Y. 2021-2022 ******************")
            print(str(obj.p1_no) + ") " + str(obj.p1_name) + " with a total votes of = " + str(pres_result))
            print("------------------------------------------------------------------------------")
        elif ((obj.pres_2 > obj.pres_1) and (obj.pres_2 > obj.pres_3)):
            print("****************** New elected President for S.Y. 2021-2022 ******************")
            print(str(obj.p2_no) + ") " + str(obj.p2_name) + " with a total votes of = " + str(pres_result))
            print("------------------------------------------------------------------------------")
        elif ((obj.pres_3 > obj.pres_1) and (obj.pres_3 > obj.pres_2)):
            print("****************** New elected President for S.Y. 2021-2022 ******************")
            print(str(obj.p3_no) + ") " + str(obj.p3_name) + " with a total votes of = " + str(pres_result))
            print("------------------------------------------------------------------------------")
        elif ((obj.pres_1 == obj.pres_2) and (obj.pres_1 > obj.pres_3) and (obj.pres_2 > obj.pres_3)):
            print("----------------------- WE HAVE A TIE -----------------------")
            print(str(obj.p1_no) + ") " + str(obj.p1_name) + " with a total votes of = " + str(pres_result))
            print(str(obj.p2_no) + ") " + str(obj.p2_name) + " with a total votes of = " + str(pres_result))
        elif ((obj.pres_2 == obj.pres_3) and (obj.pres_2 > obj.pres_1) and (obj.pres_3 > obj.pres_1)):
            print(str(obj.p2_no) + ") " + str(obj.p2_name) + " with a total votes of = " + str(pres_result))
            print(str(obj.p3_no) + ") " + str(obj.p3_name) + " with a total votes of = " + str(pres_result))
        elif ((obj.pres_1 == obj.pres_3) and (obj.pres_1 > obj.pres_2) and (obj.pres_3 > obj.pres_2)):
            print(str(obj.p1_no) + ") " + str(obj.p1_name) + " with a total votes of = " + str(pres_result))
            print(str(obj.p3_no) + ") " + str(obj.p3_name) + " with a total votes of = " + str(pres_result))
        elif ((obj.pres_1 == obj.pres_2) and (obj.pres_1 == obj.pres_3)
              and (obj.pres_2 == obj.pres_1) and (obj.pres_2 == obj.pres_3)
              and (obj.pres_3 == obj.pres_1) and (obj.pres_3 == obj.pres_2)):
            print("----------------------- WE HAVE TRIPLE TIE FOR PRESIDENT -----------------------")
            print(str(obj.p1_no) + ") " + str(obj.p1_name) + " with a total votes of = " + str(pres_result))
            print(str(obj.p2_no) + ") " + str(obj.p2_name) + " with a total votes of = " + str(pres_result))
            print(str(obj.p3_no) + ") " + str(obj.p3_name) + " with a total votes of = " + str(pres_result))
            print("------------------------------------------------------------------------------")

        # Final Result for Vice President ------------------------------------------------------------------------
        if ((obj.vpres_1 > obj.vpres_2) and (obj.vpres_1 > obj.vpres_3)):
            print("*************** New elected Vice President for S.Y. 2021-2022 ****************")
            print(str(obj.vp1_no) + ") " + str(obj.vp1_name) + " with a total votes of = " + str(vp_result))
            print("------------------------------------------------------------------------------")
        elif ((obj.vpres_2 > obj.vpres_1) and (obj.vpres_2 > obj.vpres_3)):
            print("*************** New elected Vice President for S.Y. 2021-2022 ****************")
            print(str(obj.vp2_no) + ") " + str(obj.vp2_name) + " with a total votes of = " + str(vp_result))
            print("------------------------------------------------------------------------------")
        elif ((obj.vpres_3 > obj.vpres_1) and (obj.vpres_3 > obj.vpres_2)):
            print("*************** New elected Vice President for S.Y. 2021-2022 ****************")
            print(str(obj.vp3_no) + ") " + str(obj.vp3_name) + " with a total votes of = " + str(vp_result))
            print("------------------------------------------------------------------------------")
        elif ((obj.vpres_1 == obj.vpres_2) and (obj.vpres_1 > obj.vpres_3) and (obj.vpres_2 > obj.vpres_3)):
            print("---------------------- WE HAVE A TIE FOR VICE PRESIDENT ----------------------")
            print(str(obj.vp1_no) + ") " + str(obj.vp1_name) + " with a total votes of = " + str(vp_result))
            print(str(obj.vp2_no) + ") " + str(obj.vp2_name) + " with a total votes of = " + str(vp_result))
            print("------------------------------------------------------------------------------")
        elif ((obj.vpres_2 == obj.vpres_3) and (obj.vpres_2 > obj.vpres_1) and (obj.vpres_3 > obj.vpres_1)):
            print("---------------------- WE HAVE A TIE FOR VICE PRESIDENT ----------------------")
            print(str(obj.vp2_no) + ") " + str(obj.vp2_name) + " with a total votes of = " + str(vp_result))
            print(str(obj.vp3_no) + ") " + str(obj.vp3_name) + " with a total votes of = " + str(vp_result))
            print("------------------------------------------------------------------------------")
        elif ((obj.pres_1 == obj.pres_3) and (obj.pres_1 > obj.pres_2) and (obj.pres_3 > obj.pres_2)):
            print("---------------------- WE HAVE A TIE FOR VICE PRESIDENT ----------------------")
            print(str(obj.vp1_no) + ") " + str(obj.vp1_name) + " with a total votes of = " + str(vp_result))
            print(str(obj.vp3_no) + ") " + str(obj.vp3_name) + " with a total votes of = " + str(vp_result))
            print("------------------------------------------------------------------------------")
        elif ((obj.vpres_1 == obj.vpres_2) and (obj.vpres_1 == obj.vpres_3)
              and (obj.vpres_2 == obj.pres_1) and (obj.vpres_2 == obj.vpres_3)
              and (obj.vpres_3 == obj.vpres_1) and (obj.vpres_3 == obj.vpres_2)):
            print("------------------- WE HAVE TRIPLE TIE FOR VICE PRESIDENT --------------------")
            print(str(obj.vp1_no) + ") " + str(obj.vp1_name) + " with a total votes of = " + str(vp_result))
            print(str(obj.vp2_no) + ") " + str(obj.vp2_name) + " with a total votes of = " + str(vp_result))
            print(str(obj.vp3_no) + ") " + str(obj.vp3_name) + " with a total votes of = " + str(vp_result))
            print("------------------------------------------------------------------------------")

        # Final Result for Secretary ------------------------------------------------------------------------
        if ((obj.sec_1 > obj.sec_2) and (obj.sec_1 > obj.sec_3)):
            print("***************** New elected Secretary for S.Y. 2021-2022 *******************")
            print(str(obj.sec1_no) + ") " + str(obj.sec1_name) + " with a total votes of = " + str(sec_result))
            print("------------------------------------------------------------------------------")
        elif ((obj.sec_2 > obj.sec_1) and (obj.sec_2 > obj.sec_3)):
            print("***************** New elected Secretary for S.Y. 2021-2022 *******************")
            print(str(obj.sec2_no) + ") " + str(obj.sec2_name) + " with a total votes of = " + str(sec_result))
            print("------------------------------------------------------------------------------")
        elif ((obj.sec_3 > obj.sec_1) and (obj.sec_3 > obj.sec_2)):
            print("***************** New elected Secretary for S.Y. 2021-2022 *******************")
            print(str(obj.sec3_no) + ") " + str(obj.sec3_name) + " with a total votes of = " + str(sec_result))
            print("------------------------------------------------------------------------------")
        elif ((obj.sec_1 == obj.sec_2) and (obj.sec_1 > obj.sec_3) and (obj.sec_2 > obj.sec_3)):
            print("------------------------ WE HAVE A TIE FOR SECRETARY -------------------------")
            print(str(obj.sec1_no) + ") " + str(obj.sec1_name) + " with a total votes of = " + str(sec_result))
            print(str(obj.sec2_no) + ") " + str(obj.sec2_name) + " with a total votes of = " + str(sec_result))
            print("------------------------------------------------------------------------------")
        elif ((obj.sec_2 == obj.sec_3) and (obj.sec_2 > obj.sec_1) and (obj.sec_3 > obj.sec_1)):
            print("------------------------ WE HAVE A TIE FOR SECRETARY -------------------------")
            print(str(obj.sec2_no) + ") " + str(obj.sec2_name) + " with a total votes of = " + str(sec_result))
            print(str(obj.sec3_no) + ") " + str(obj.sec3_name) + " with a total votes of = " + str(sec_result))
            print("------------------------------------------------------------------------------")
        elif ((obj.sec_1 == obj.sec_3) and (obj.sec_1 > obj.sec_2) and (obj.sec_3 > obj.sec_2)):
            print("------------------------ WE HAVE A TIE FOR SECRETARY -------------------------")
            print(str(obj.sec1_no) + ") " + str(obj.sec1_name) + " with a total votes of = " + str(sec_result))
            print(str(obj.sec3_no) + ") " + str(obj.sec3_name) + " with a total votes of = " + str(sec_result))
            print("------------------------------------------------------------------------------")
        elif ((obj.sec_1 == obj.sec_2) and (obj.sec_1 == obj.sec_3)
              and (obj.sec_2 == obj.sec_1) and (obj.sec_2 == obj.sec_3)
              and (obj.sec_3 == obj.sec_1) and (obj.sec_3 == obj.sec_2)):
            print("---------------------- WE HAVE TRIPLE TIE FOR SECRETARY ----------------------")
            print(str(obj.sec1_no) + ") " + str(obj.sec1_name) + " with a total votes of = " + str(sec_result))
            print(str(obj.sec2_no) + ") " + str(obj.sec2_name) + " with a total votes of = " + str(sec_result))
            print(str(obj.sec3_no) + ") " + str(obj.sec3_name) + " with a total votes of = " + str(sec_result))
            print("------------------------------------------------------------------------------")

        # Final Result for Auditor ------------------------------------------------------------------------
        if ((obj.aud_1 > obj.aud_2) and (obj.aud_1 > obj.aud_3)):
            print("****************** New elected Auditor for S.Y. 2021-2022 ********************")
            print(str(obj.aud1_no) + ") " + str(obj.aud1_name) + " with a total votes of = " + str(aud_result))
            print("------------------------------------------------------------------------------")
        elif ((obj.aud_2 > obj.aud_1) and (obj.aud_2 > obj.aud_3)):
            print("****************** New elected Auditor for S.Y. 2021-2022 ********************")
            print(str(obj.aud2_no) + ") " + str(obj.aud2_name) + " with a total votes of = " + str(aud_result))
            print("------------------------------------------------------------------------------")
        elif ((obj.aud_3 > obj.aud_1) and (obj.aud_3 > obj.aud_2)):
            print("****************** New elected Auditor for S.Y. 2021-2022 ********************")
            print(str(obj.aud3_no) + ") " + str(obj.aud3_name) + " with a total votes of = " + str(aud_result))
            print("------------------------------------------------------------------------------")
        elif ((obj.aud_1 == obj.aud_2) and (obj.aud_1 > obj.aud_3) and (obj.aud_2 > obj.aud_3)):
            print("------------------------- WE HAVE A TIE FOR AUDITOR --------------------------")
            print(str(obj.aud1_no) + ") " + str(obj.aud1_name) + " with a total votes of = " + str(aud_result))
            print(str(obj.aud2_no) + ") " + str(obj.aud2_name) + " with a total votes of = " + str(aud_result))
            print("------------------------------------------------------------------------------")
        elif ((obj.aud_2 == obj.aud_3) and (obj.aud_2 > obj.aud_1) and (obj.aud_3 > obj.aud_1)):
            print("------------------------- WE HAVE A TIE FOR AUDITOR --------------------------")
            print(str(obj.aud2_no) + ") " + str(obj.aud2_name) + " with a total votes of = " + str(aud_result))
            print(str(obj.aud3_no) + ") " + str(obj.aud3_name) + " with a total votes of = " + str(aud_result))
            print("------------------------------------------------------------------------------")
        elif ((obj.aud_1 == obj.aud_3) and (obj.aud_1 > obj.aud_2) and (obj.aud_3 > obj.aud_2)):
            print("------------------------- WE HAVE A TIE FOR AUDITOR --------------------------")
            print(str(obj.aud1_no) + ") " + str(obj.aud1_name) + " with a total votes of = " + str(aud_result))
            print(str(obj.aud3_no) + ") " + str(obj.aud3_name) + " with a total votes of = " + str(aud_result))
            print("------------------------------------------------------------------------------")
        elif ((obj.aud_1 == obj.aud_2) and (obj.aud_1 == obj.aud_3)
              and (obj.aud_2 == obj.aud_1) and (obj.aud_2 == obj.aud_3)
              and (obj.aud_3 == obj.aud_1) and (obj.aud_3 == obj.aud_2)):
            print("---------------------- WE HAVE TRIPLE TIE FOR AUDITOR ------------------------")
            print(str(obj.aud1_no) + ") " + str(obj.aud1_name) + " with a total votes of = " + str(aud_result))
            print(str(obj.aud2_no) + ") " + str(obj.aud2_name) + " with a total votes of = " + str(aud_result))
            print(str(obj.aud3_no) + ") " + str(obj.aud3_name) + " with a total votes of = " + str(aud_result))
            print("------------------------------------------------------------------------------")

        # Final Result for Treasurer ------------------------------------------------------------------------
        if ((obj.tre_1 > obj.tre_2) and (obj.tre_1 > obj.tre_3)):
            print("***************** New elected Treasurer for S.Y. 2021-2022 *******************")
            print(str(obj.tre1_no) + ") " + str(obj.tre1_name) + " with a total votes of = " + str(tre_result))
            print("------------------------------------------------------------------------------")
        elif ((obj.tre_2 > obj.tre_1) and (obj.tre_2 > obj.tre_3)):
            print("***************** New elected Treasurer for S.Y. 2021-2022 *******************")
            print(str(obj.tre2_no) + ") " + str(obj.tre2_name) + " with a total votes of = " + str(tre_result))
            print("------------------------------------------------------------------------------")
        elif ((obj.tre_3 > obj.tre_1) and (obj.tre_3 > obj.tre_2)):
            print("***************** New elected Treasurer for S.Y. 2021-2022 *******************")
            print(str(obj.tre3_no) + ") " + str(obj.tre3_name) + " with a total votes of = " + str(tre_result))
            print("------------------------------------------------------------------------------")
        elif ((obj.tre_1 == obj.tre_2) and (obj.tre_1 > obj.tre_3) and (obj.tre_2 > obj.tre_3)):
            print("------------------------ WE HAVE A TIE FOR TREASURER -------------------------")
            print(str(obj.tre1_no) + ") " + str(obj.tre1_name) + " with a total votes of = " + str(tre_result))
            print(str(obj.tre2_no) + ") " + str(obj.tre2_name) + " with a total votes of = " + str(tre_result))
            print("------------------------------------------------------------------------------")
        elif ((obj.tre_2 == obj.tre_3) and (obj.tre_2 > obj.tre_1) and (obj.tre_3 > obj.tre_1)):
            print("------------------------ WE HAVE A TIE FOR TREASURER -------------------------")
            print(str(obj.tre2_no) + ") " + str(obj.tre2_name) + " with a total votes of = " + str(tre_result))
            print(str(obj.tre3_no) + ") " + str(obj.tre3_name) + " with a total votes of = " + str(tre_result))
            print("------------------------------------------------------------------------------")
        elif ((obj.tre_1 == obj.tre_3) and (obj.tre_1 > obj.tre_2) and (obj.sec_3 > obj.tre_2)):
            print("------------------------ WE HAVE A TIE FOR TREASURER -------------------------")
            print(str(obj.tre1_no) + ") " + str(obj.tre1_name) + " with a total votes of = " + str(tre_result))
            print(str(obj.tre3_no) + ") " + str(obj.tre3_name) + " with a total votes of = " + str(tre_result))
            print("------------------------------------------------------------------------------")
        elif ((obj.tre_1 == obj.tre_2) and (obj.tre_1 == obj.tre_3)
              and (obj.tre_2 == obj.tre_1) and (obj.tre_2 == obj.tre_3)
              and (obj.tre_3 == obj.tre_1) and (obj.tre_3 == obj.tre_2)):
            print("---------------------- WE HAVE TRIPLE TIE FOR TREASURER ----------------------")
            print(str(obj.tre1_no) + ") " + str(obj.tre1_name) + " with a total votes of = " + str(tre_result))
            print(str(obj.tre2_no) + ") " + str(obj.tre2_name) + " with a total votes of = " + str(tre_result))
            print(str(obj.tre3_no) + ") " + str(obj.tre3_name) + " with a total votes of = " + str(tre_result))
            print("------------------------------------------------------------------------------")

        # Final Result for Media Information ------------------------------------------------------------------------
        if ((obj.media_1 > obj.media_2) and (obj.media_1 > obj.media_3)):
            print("************ New elected Media Information for S.Y. 2021-2022 ****************")
            print(str(obj.media1_no) + ") " + str(obj.media1_name) + " with a total votes of = " + str(media_result))
            print("------------------------------------------------------------------------------")
        elif ((obj.media_2 > obj.media_1) and (obj.media_2 > obj.media_3)):
            print("************ New elected Media Information for S.Y. 2021-2022 ****************")
            print(str(obj.media2_no) + ") " + str(obj.media2_name) + " with a total votes of = " + str(media_result))
            print("------------------------------------------------------------------------------")
        elif ((obj.media_3 > obj.media_1) and (obj.media_3 > obj.media_2)):
            print("************ New elected Media Information for S.Y. 2021-2022 ****************")
            print(str(obj.media3_no) + ") " + str(obj.media3_name) + " with a total votes of = " + str(media_result))
            print("------------------------------------------------------------------------------")
        elif ((obj.media_1 == obj.media_2) and (obj.media_1 > obj.media_3) and (obj.media_2 > obj.media_3)):
            print("-------------------- WE HAVE A TIE FOR MEDIA INFORMATION ---------------------")
            print(str(obj.media1_no) + ") " + str(obj.media1_name) + " with a total votes of = " + str(media_result))
            print(str(obj.media2_no) + ") " + str(obj.media2_name) + " with a total votes of = " + str(media_result))
            print("------------------------------------------------------------------------------")
        elif ((obj.media_2 == obj.media_3) and (obj.media_2 > obj.media_1) and (obj.media_3 > obj.media_1)):
            print("-------------------- WE HAVE A TIE FOR MEDIA INFORMATION ---------------------")
            print(str(obj.media2_no) + ") " + str(obj.media2_name) + " with a total votes of = " + str(media_result))
            print(str(obj.media3_no) + ") " + str(obj.media3_name) + " with a total votes of = " + str(media_result))
            print("------------------------------------------------------------------------------")
        elif ((obj.media_1 == obj.media_3) and (obj.media_1 > obj.media_2) and (obj.media_3 > obj.media_2)):
            print("-------------------- WE HAVE A TIE FOR MEDIA INFORMATION ---------------------")
            print(str(obj.media1_no) + ") " + str(obj.media1_name) + " with a total votes of = " + str(media_result))
            print(str(obj.media3_no) + ") " + str(obj.media3_name) + " with a total votes of = " + str(media_result))
            print("------------------------------------------------------------------------------")
        elif ((obj.media_1 == obj.media_2) and (obj.media_1 == obj.media_3)
              and (obj.media_2 == obj.media_1) and (obj.media_2 == obj.media_3)
              and (obj.media_3 == obj.media_1) and (obj.media_3 == obj.media_2)):
            print("----------------- WE HAVE TRIPLE TIE FOR MEDIA INFORMATION -------------------")
            print(str(obj.media1_no) + ") " + str(obj.media1_name) + " with a total votes of = " + str(media_result))
            print(str(obj.media2_no) + ") " + str(obj.media2_name) + " with a total votes of = " + str(media_result))
            print(str(obj.media3_no) + ") " + str(obj.media3_name) + " with a total votes of = " + str(media_result))
            print("------------------------------------------------------------------------------")

        # Final Result for First Year Representative ------------------------------------------------------------------------
        if ((obj.f_rep_1 > obj.f_rep_2) and (obj.f_rep_1 > obj.f_rep_3)):
            print("******** New elected First Year Representative for S.Y. 2021-2022 ************")
            print(str(obj.f_rep1_no) + ") " + str(obj.f_rep1_name) + " with a total votes of = " + str(f_rep_result))
            print("------------------------------------------------------------------------------")
        elif ((obj.f_rep_2 > obj.f_rep_1) and (obj.f_rep_2 > obj.f_rep_3)):
            print("******** New elected First Year Representative for S.Y. 2021-2022 ************")
            print(str(obj.f_rep2_no) + ") " + str(obj.f_rep2_name) + " with a total votes of = " + str(f_rep_result))
            print("------------------------------------------------------------------------------")
        elif ((obj.f_rep_3 > obj.f_rep_1) and (obj.f_rep_3 > obj.f_rep_2)):
            print("******** New elected First Year Representative for S.Y. 2021-2022 ************")
            print(str(obj.f_rep3_no) + ") " + str(obj.f_rep3_name) + " with a total votes of = " + str(f_rep_result))
            print("------------------------------------------------------------------------------")
        elif ((obj.f_rep_1 == obj.f_rep_2) and (obj.f_rep_1 > obj.f_rep_3) and (obj.f_rep_2 > obj.f_rep_3)):
            print("--------------- WE HAVE A TIE FOR FIRST YEAR REPRESENTATIVE ------------------")
            print(str(obj.f_rep1_no) + ") " + str(obj.f_rep1_name) + " with a total votes of = " + str(f_rep_result))
            print(str(obj.f_rep2_no) + ") " + str(obj.f_rep2_name) + " with a total votes of = " + str(f_rep_result))
            print("------------------------------------------------------------------------------")
        elif ((obj.f_rep_2 == obj.f_rep_3) and (obj.f_rep_2 > obj.f_rep_1) and (obj.f_rep_3 > obj.f_rep_1)):
            print("--------------- WE HAVE A TIE FOR FIRST YEAR REPRESENTATIVE ------------------")
            print(str(obj.f_rep2_no) + ") " + str(obj.f_rep2_name) + " with a total votes of = " + str(f_rep_result))
            print(str(obj.f_rep3_no) + ") " + str(obj.f_rep3_name) + " with a total votes of = " + str(f_rep_result))
            print("------------------------------------------------------------------------------")
        elif ((obj.f_rep_1 == obj.f_rep_3) and (obj.f_rep_1 > obj.f_rep_2) and (obj.f_rep_3 > obj.f_rep_2)):
            print("--------------- WE HAVE A TIE FOR FIRST YEAR REPRESENTATIVE ------------------")
            print(str(obj.f_rep1_no) + ") " + str(obj.f_rep1_name) + " with a total votes of = " + str(f_rep_result))
            print(str(obj.f_rep3_no) + ") " + str(obj.f_rep3_name) + " with a total votes of = " + str(f_rep_result))
            print("------------------------------------------------------------------------------")
        elif ((obj.f_rep_1 == obj.f_rep_2) and (obj.f_rep_1 == obj.f_rep_3)
              and (obj.f_rep_2 == obj.f_rep_1) and (obj.f_rep_2 == obj.f_rep_3)
              and (obj.f_rep_3 == obj.f_rep_1) and (obj.f_rep_3 == obj.f_rep_2)):
            print("------------ WE HAVE TRIPLE TIE FOR FIRST YEAR REPRESENTATIVE ----------------")
            print(str(obj.f_rep1_no) + ") " + str(obj.f_rep1_name) + " with a total votes of = " + str(f_rep_result))
            print(str(obj.f_rep2_no) + ") " + str(obj.f_rep2_name) + " with a total votes of = " + str(f_rep_result))
            print(str(obj.f_rep3_no) + ") " + str(obj.f_rep3_name) + " with a total votes of = " + str(f_rep_result))
            print("------------------------------------------------------------------------------")

        # Final Result for Second Year Representative ------------------------------------------------------------------------
        if ((obj.s_rep_1 > obj.s_rep_2) and (obj.s_rep_1 > obj.s_rep_3)):
            print("******** New elected Second Year Representative for S.Y. 2021-2022 ***********")
            print(str(obj.s_rep1_no) + ") " + str(obj.s_rep1_name) + " with a total votes of = " + str(s_rep_result))
            print("------------------------------------------------------------------------------")
        elif ((obj.s_rep_2 > obj.s_rep_1) and (obj.s_rep_2 > obj.s_rep_3)):
            print("******** New elected Second Year Representative for S.Y. 2021-2022 ***********")
            print(str(obj.s_rep2_no) + ") " + str(obj.s_rep2_name) + " with a total votes of = " + str(s_rep_result))
            print("------------------------------------------------------------------------------")
        elif ((obj.s_rep_3 > obj.s_rep_1) and (obj.s_rep_3 > obj.s_rep_2)):
            print("******** New elected Second Year Representative for S.Y. 2021-2022 ***********")
            print(str(obj.s_rep3_no) + ") " + str(obj.s_rep3_name) + " with a total votes of = " + str(s_rep_result))
            print("------------------------------------------------------------------------------")
        elif ((obj.s_rep_1 == obj.s_rep_2) and (obj.s_rep_1 > obj.s_rep_3) and (obj.s_rep_2 > obj.s_rep_3)):
            print("--------------- WE HAVE A TIE FOR SECOND YEAR REPRESENTATIVE -----------------")
            print(str(obj.s_rep1_no) + ") " + str(obj.s_rep1_name) + " with a total votes of = " + str(s_rep_result))
            print(str(obj.s_rep2_no) + ") " + str(obj.s_rep2_name) + " with a total votes of = " + str(s_rep_result))
            print("------------------------------------------------------------------------------")
        elif ((obj.s_rep_2 == obj.s_rep_3) and (obj.s_rep_2 > obj.s_rep_1) and (obj.s_rep_3 > obj.s_rep_1)):
            print("--------------- WE HAVE A TIE FOR SECOND YEAR REPRESENTATIVE -----------------")
            print(str(obj.s_rep2_no) + ") " + str(obj.s_rep2_name) + " with a total votes of = " + str(s_rep_result))
            print(str(obj.s_rep3_no) + ") " + str(obj.s_rep3_name) + " with a total votes of = " + str(s_rep_result))
            print("------------------------------------------------------------------------------")
        elif ((obj.s_rep_1 == obj.s_rep_3) and (obj.s_rep_1 > obj.s_rep_2) and (obj.s_rep_3 > obj.s_rep_2)):
            print("--------------- WE HAVE A TIE FOR SECOND YEAR REPRESENTATIVE -----------------")
            print(str(obj.s_rep1_no) + ") " + str(obj.s_rep1_name) + " with a total votes of = " + str(s_rep_result))
            print(str(obj.s_rep3_no) + ") " + str(obj.s_rep3_name) + " with a total votes of = " + str(s_rep_result))
            print("------------------------------------------------------------------------------")
        elif ((obj.s_rep_1 == obj.s_rep_2) and (obj.s_rep_1 == obj.s_rep_3)
              and (obj.s_rep_2 == obj.s_rep_1) and (obj.s_rep_2 == obj.s_rep_3)
              and (obj.s_rep_3 == obj.s_rep_1) and (obj.s_rep_3 == obj.s_rep_2)):
            print("------------ WE HAVE TRIPLE TIE FOR SECOND YEAR REPRESENTATIVE ---------------")
            print(str(obj.s_rep1_no) + ") " + str(obj.s_rep1_name) + " with a total votes of = " + str(s_rep_result))
            print(str(obj.s_rep2_no) + ") " + str(obj.s_rep2_name) + " with a total votes of = " + str(s_rep_result))
            print(str(obj.s_rep3_no) + ") " + str(obj.s_rep3_name) + " with a total votes of = " + str(s_rep_result))
            print("------------------------------------------------------------------------------")

        # Final Result for Third Year Representative ------------------------------------------------------------------------
        if ((obj.t_rep_1 > obj.t_rep_2) and (obj.t_rep_1 > obj.t_rep_3)):
            print("********* New elected Third Year Representative for S.Y. 2021-2022 ***********")
            print(str(obj.t_rep1_no) + ") " + str(obj.t_rep1_name) + " with a total votes of = " + str(t_rep_result))
            print("------------------------------------------------------------------------------")
        elif ((obj.t_rep_2 > obj.t_rep_1) and (obj.t_rep_2 > obj.t_rep_3)):
            print("********* New elected Third Year Representative for S.Y. 2021-2022 ***********")
            print(str(obj.t_rep2_no) + ") " + str(obj.t_rep2_name) + " with a total votes of = " + str(t_rep_result))
            print("------------------------------------------------------------------------------")
        elif ((obj.t_rep_3 > obj.t_rep_1) and (obj.t_rep_3 > obj.t_rep_2)):
            print("********* New elected Third Year Representative for S.Y. 2021-2022 ***********")
            print(str(obj.t_rep3_no) + ") " + str(obj.t_rep3_name) + " with a total votes of = " + str(t_rep_result))
            print("------------------------------------------------------------------------------")
        elif ((obj.t_rep_1 == obj.t_rep_2) and (obj.t_rep_1 > obj.t_rep_3) and (obj.t_rep_2 > obj.t_rep_3)):
            print("---------------- WE HAVE A TIE FOR THIRD YEAR REPRESENTATIVE -----------------")
            print(str(obj.t_rep1_no) + ") " + str(obj.t_rep1_name) + " with a total votes of = " + str(t_rep_result))
            print(str(obj.t_rep2_no) + ") " + str(obj.t_rep2_name) + " with a total votes of = " + str(t_rep_result))
            print("------------------------------------------------------------------------------")
        elif ((obj.t_rep_2 == obj.t_rep_3) and (obj.t_rep_2 > obj.t_rep_1) and (obj.t_rep_3 > obj.t_rep_1)):
            print("---------------- WE HAVE A TIE FOR THIRD YEAR REPRESENTATIVE -----------------")
            print(str(obj.t_rep2_no) + ") " + str(obj.t_rep2_name) + " with a total votes of = " + str(t_rep_result))
            print(str(obj.t_rep3_no) + ") " + str(obj.t_rep3_name) + " with a total votes of = " + str(t_rep_result))
            print("------------------------------------------------------------------------------")
        elif ((obj.t_rep_1 == obj.t_rep_3) and (obj.t_rep_1 > obj.t_rep_2) and (obj.t_rep_3 > obj.t_rep_2)):
            print("---------------- WE HAVE A TIE FOR THIRD YEAR REPRESENTATIVE -----------------")
            print(str(obj.t_rep1_no) + ") " + str(obj.t_rep1_name) + " with a total votes of = " + str(t_rep_result))
            print(str(obj.t_rep3_no) + ") " + str(obj.t_rep3_name) + " with a total votes of = " + str(t_rep_result))
            print("------------------------------------------------------------------------------")
        elif ((obj.t_rep_1 == obj.t_rep_2) and (obj.t_rep_1 == obj.t_rep_3)
              and (obj.t_rep_2 == obj.t_rep_1) and (obj.t_rep_2 == obj.t_rep_3)
              and (obj.t_rep_3 == obj.t_rep_1) and (obj.t_rep_3 == obj.t_rep_2)):
            print("------------- WE HAVE TRIPLE TIE FOR THIRD YEAR REPRESENTATIVE ---------------")
            print(str(obj.t_rep1_no) + ") " + str(obj.t_rep1_name) + " with a total votes of = " + str(t_rep_result))
            print(str(obj.t_rep2_no) + ") " + str(obj.t_rep2_name) + " with a total votes of = " + str(t_rep_result))
            print(str(obj.t_rep3_no) + ") " + str(obj.t_rep3_name) + " with a total votes of = " + str(t_rep_result))
            print("------------------------------------------------------------------------------")

        # Final Result for Fourth Year Representative ------------------------------------------------------------------------
        if ((obj.frt_rep_1 > obj.frt_rep_2) and (obj.frt_rep_1 > obj.frt_rep_3)):
            print("******** New elected Fourth Year Representative for S.Y. 2021-2022 ***********")
            print(str(obj.frt_rep1_no) + ") " + str(obj.frt_rep1_name) + " with a total votes of = " + str(frt_rep_result))
            print("------------------------------------------------------------------------------")
        elif ((obj.frt_rep_2 > obj.frt_rep_1) and (obj.frt_rep_2 > obj.frt_rep_3)):
            print("******** New elected Fourth Year Representative for S.Y. 2021-2022 ***********")
            print(str(obj.frt_rep2_no) + ") " + str(obj.frt_rep2_name) + " with a total votes of = " + str(frt_rep_result))
            print("------------------------------------------------------------------------------")
        elif ((obj.frt_rep_3 > obj.frt_rep_1) and (obj.frt_rep_3 > obj.frt_rep_2)):
            print("******** New elected Fourth Year Representative for S.Y. 2021-2022 ***********")
            print(str(obj.frt_rep3_no) + ") " + str(obj.frt_rep3_name) + " with a total votes of = " + str(frt_rep_result))
            print("------------------------------------------------------------------------------")
        elif ((obj.frt_rep_1 == obj.frt_rep_2) and (obj.frt_rep_1 > obj.frt_rep_3) and (obj.frt_rep_2 > obj.frt_rep_3)):
            print("--------------- WE HAVE A TIE FOR FOURTH YEAR REPRESENTATIVE -----------------")
            print(str(obj.frt_rep1_no) + ") " + str(obj.frt_rep1_name) + " with a total votes of = " + str(frt_rep_result))
            print(str(obj.frt_rep2_no) + ") " + str(obj.frt_rep2_name) + " with a total votes of = " + str(frt_rep_result))
            print("------------------------------------------------------------------------------")
        elif ((obj.frt_rep_2 == obj.frt_rep_3) and (obj.frt_rep_2 > obj.frt_rep_1) and (obj.frt_rep_3 > obj.frt_rep_1)):
            print("--------------- WE HAVE A TIE FOR FOURTH YEAR REPRESENTATIVE -----------------")
            print(str(obj.frt_rep2_no) + ") " + str(obj.frt_rep2_name) + " with a total votes of = " + str(frt_rep_result))
            print(str(obj.frt_rep3_no) + ") " + str(obj.frt_rep3_name) + " with a total votes of = " + str(frt_rep_result))
            print("------------------------------------------------------------------------------")
        elif ((obj.frt_rep_1 == obj.frt_rep_3) and (obj.frt_rep_1 > obj.frt_rep_2) and (obj.frt_rep_3 > obj.frt_rep_2)):
            print("--------------- WE HAVE A TIE FOR FOURTH YEAR REPRESENTATIVE -----------------")
            print(str(obj.frt_rep1_no) + ") " + str(obj.frt_rep1_name) + " with a total votes of = " + str(frt_rep_result))
            print(str(obj.frt_rep3_no) + ") " + str(obj.frt_rep3_name) + " with a total votes of = " + str(frt_rep_result))
            print("------------------------------------------------------------------------------")
        elif ((obj.frt_rep_1 == obj.frt_rep_2) and (obj.frt_rep_1 == obj.frt_rep_3)
              and (obj.frt_rep_2 == obj.frt_rep_1) and (obj.frt_rep_2 == obj.frt_rep_3)
              and (obj.frt_rep_3 == obj.frt_rep_1) and (obj.frt_rep_3 == obj.frt_rep_2)):
            print("------------ WE HAVE TRIPLE TIE FOR FOURTH YEAR REPRESENTATIVE ---------------")
            print(str(obj.frt_rep1_no) + ") " + str(obj.frt_rep1_name) + " with a total votes of = " + str(frt_rep_result))
            print(str(obj.frt_rep2_no) + ") " + str(obj.frt_rep2_name) + " with a total votes of = " + str(frt_rep_result))
            print(str(obj.frt_rep3_no) + ") " + str(obj.frt_rep3_name) + " with a total votes of = " + str(frt_rep_result))
            print("------------------------------------------------------------------------------")
        else:
            print("System error. Please try again.")


#Calling functions--------------------------------------------
call = election()
call.welcome()
call.registration()