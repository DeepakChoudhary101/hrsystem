from django.urls import path

from . import views



urlpatterns = [

    path('',views.index,name="index"),

    path('assign_permission/', views.assign_permission, name='assign_permission'),

    path('permission_page/', views.permission_page, name='permission_page'),

    path('Call_to_action',views.Call_to_action,name="Call_to_action"),

    path('Contact_us',views.Contact_us,name="Contact_us"),

    path('thank_you',views.thank_you,name='thank_you'),

    path('data_scientist',views.Data_scientist,name='data_scientist'),

    path('machine_learning',views.Machine_learning,name='machine_learning'),

    path('research_scientist',views.Research_scientist_engineer,name='research_scientist'),

    path('software_application',views.Software_application,name='software_application'),

    path('career', views.career, name='career'),

    path('login/',views.user_login,name='login'),

    path('page_not_found/',views.page_not_found,name='page_not_found'),

    path('logout/',views.user_logout,name='logout'),

    path('dashboard/',views.dashboard,name='dashboard'),

    path('apply_candidate/',views.apply_candidate,name='apply_candidate'),



    path('update_candidate/<int:candidate_id>/', views.update_candidate, name='update_candidate'),



path('remove_new_data_indicator/', views.remove_new_data_indicator, name='remove_new_data_indicator'),



path('accept1/<int:candidate_id>/',views.accept1,name='accept1'),



path('remove_candidate_data/<int:candidate_id>/', views.remove_candidate_data, name='remove_candidate_data'),



path('pending/',views.pending,name='pending'),



path('inter/',views.inter,name='inter'),
path('Save_score_data_scientist_technical/<int:candidate_id>/',views.Save_score_data_scientist_technical,name='Save_score_data_scientist_technical'),
path('update_marks',views.update_marks,name="update_marks"),


path('take_interview/<int:candidate_id>/',views.take_interview,name='take_interview'),
path('show_technical_score/<int:candidate_id>/',views.show_technical_score,name='show_technical_score'),



path('interview/<int:candidate_id>/', views.candidate_decision, name='interview'),



path('reject_candidates/', views.reject_candidates, name='reject_candidates'),



path('reject_candidate/<int:candidate_id>/', views.reject_candidate, name='reject_candidate'),



path('confirm_otp_data_scientist/<int:candidate_id>/', views.confirm_otp_data_scientist, name='confirm_otp_data_scientist'),

path('confirm_otp_software_developer/<int:candidate_id>/', views.confirm_otp_software_developer, name='confirm_otp_software_developer'),

path('confirm_otp_machine_learning/<int:candidate_id>/', views.confirm_otp_machine_learning, name='confirm_otp_machine_learning'),

path('confirm_otp_research_scientist/<int:candidate_id>/', views.confirm_otp_research_scientist, name='confirm_otp_research_scientist'),





path('machine_learning/<int:candidate_id>/',views.machine_learning,name='machine_learning'),



path('save_scores_technical/<int:candidate_id>/', views.save_scores_technical, name='save_scores_technical'),

path('save_scores_coding/<int:candidate_id>/', views.save_scores_coding, name='save_scores_coding'),



path('confirmation/', views.confirmation_page, name='confirmation_page'),



path('display_scores/', views.display_scores, name='display_scores'),



path('selected_candidate/',views.selected_candidate,name='selected_candidate'),



path('send-invitation/<int:candidate_id>/', views.send_invitation_technical, name='send_invitation_technical'),



path('select-interview-dates/', views.select_interview_dates_technical, name='select_interview_dates_technical'),



path('select-interview-dates1/', views.select_interview_dates_coding, name='select_interview_dates_coding'),



path('show-dates/<int:candidate_id>/', views.show_dates_technical, name='show_dates_technical'),



path('show-dates1/<int:candidate_id>/', views.show_dates_coding, name='show_dates_coding'),



path('send-zoom-invitation1/<int:candidate_id>/<str:selected_date>/', views.send_zoom_invitation_coding, name='send_zoom_invitation_coding'),



path('send-zoom-invitation/<int:candidate_id>/<str:selected_date>/', views.send_zoom_invitation_technical, name='send_zoom_invitation_technical'),



path('send-invitation1/<int:candidate_id>/', views.send_invitation_coding, name='send_invitation_coding'),



# path('confirm_code/<int:candidate_id>/<str:selected_subject>/<str:user_message>/<str:name>/<str:user_email>/', views.confirm_code, name='confirm_code'),

path('Max_code',views.Max_code,name="Max_code"),

path('Max_apply',views.Max_apply,name='Max_apply'),



path('confirm_code/<int:user_id>/<str:selected_subject>/<str:user_message>/<str:user_name>/<str:user_email>/', views.confirm_code, name='confirm_code'),

path('Data_scientist',views.Data_scientist_apply,name='Data_scientist'),

path('Machine_learning_engineer',views.Machine_learning_engineer_apply,name='Machine_learning_engineer'),

path('Research_scientist',views.Research_scientist_apply,name='Research_scientist'),

path('Software_application_developer',views.Software_application_developer_apply,name='Software_application_developer'),

path('software_details/<int:candidate_id>/',views.software_details,name='software_details'),

path('Research_details/<int:candidate_id>/',views.Research_details,name='Research_details'),

path('Machine_details/<int:candidate_id>/',views.Machine_details,name='Machine_details'),

path('Data_details/<int:candidate_id>/',views.Data_details,name='Data_details'),

path('interview_process_view/<int:candidate_id>/',views.interview_process_view,name="interview_process_view"),

path('rejectdata/<int:candidate_id>/',views.rejectdata,name='rejectdata'),

path('rejection_reason/<int:candidate_id>/',views.rejection_reason,name='rejection_reason'),

path('review_salary/<int:candidate_id>/',views.review_salary,name="review_salary"),
path('Selected_candidates',views.Selected_candidates,name='Selected_candidates'),

       







]

