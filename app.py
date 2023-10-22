#################################################################
import os, sys
######################################################################################################
level_up_folders = 2
level_up_string = "/.." * level_up_folders + "/"
sys.path.insert(1, os.path.abspath(__file__ + level_up_string))
# st.write((1, os.path.abspath(__file__ + level_up_string)))
######################################################################################################
## Importing Libraries
from functions_preprocess import *
warnings.filterwarnings('ignore')
warnings.filterwarnings("ignore", category=DeprecationWarning)
######################################################################################################
## Disable Warnings
st.set_option('deprecation.showPyplotGlobalUse'     , False)
st.set_option('deprecation.showfileUploaderEncoding', False)
st.set_page_config(
    layout     = "wide",
    page_title = "Career Simulation",
    page_icon  = "yammer.ico",
)
################################################### Defining Static Data ###############################################
user_color   = '#337FBF'
title_webapp = "Career Simulation"
image_link   = "data:image/jpeg;base64,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"

html_temp = f"""
            <div style="background-color:{user_color};padding:12px">
            <h1 style="color:white;text-align:center;">{title_webapp}
            <img src = "{image_link}" align="right" width=75px ></h1>
            </div>
            """
st.markdown(html_temp, unsafe_allow_html=True)
################################################### Defining Static Paths ##############################################
# data_file_folder = os.path.join('data', 'Original Data', data_folder)
# results_file_folder = os.path.join('results', 'Original Data', data_folder)

# files_dir_orig = os.path.dirname(os.getcwd())
# base_path = os.getcwd()
base_path = os.path.abspath(__file__ + level_up_string)

DOWNLOADS_PATH = os.path.join(base_path, "downloads")
if not os.path.exists(DOWNLOADS_PATH):
    os.mkdir(DOWNLOADS_PATH)

dataset_path = os.path.join(base_path, 'data')
##############################################################################
## Log File
logs_folder = os.path.join(base_path, "code_run_logs")
if not os.path.exists(logs_folder):
    os.mkdir(logs_folder)
log_file_path = os.path.join(logs_folder, "Running_Logs_Demo.txt")
with open(log_file_path, "a") as datafile:
    print('------------------------------------------------------------', file=datafile)
    print(f'Code started at : {datetime.datetime.now()}', file=datafile)
#################################################################
## Functions
########################

################################################################
home_selected = option_menu(None,
                           ['Data Import',
                            'Career Visualization',
                            ],
                           icons=['download', 'graph-up'],
                           ## icons from website: https://icons.getbootstrap.com/
                           menu_icon="cast", default_index=0, orientation="horizontal")
################################################################
if   home_selected == 'Data Import':
    st.info(f'Looking for data in path :{os.path.join(dataset_path)}')
    files_available1 = [f for f in glob.glob(os.path.join(dataset_path, "*.csv"))]
    files_available2 = [f for f in glob.glob(os.path.join(dataset_path, "*.xls"))]
    files_available = files_available1 + files_available2

    files_name = [f.replace(dataset_path, '').replace('\\', '').replace('/', '') for f in
                  files_available]

    dataset_dropdown = st.selectbox("Please select the file to choose", (['None'] + files_name))

    dataset_flag = 0

    if dataset_dropdown != 'None':
        if dataset_dropdown.endswith('.csv'):
            df_dateset = pd.read_csv(os.path.join(dataset_path, dataset_dropdown), dtype='str')
        elif dataset_dropdown.endswith('.xls'):
            df_dateset = pd.read_excel(os.path.join(dataset_path, dataset_dropdown), dtype='str')

        if st.checkbox('Click to view', value=True):
            st.dataframe(df_dateset.head())
            st.write(df_dateset.shape)

            # st.write(df_dateset['message_type'].value_counts())

        col_1, col_2 = st.columns(2)
        df_orig = read_process_data(os.path.join(dataset_path, dataset_dropdown))

        if st.checkbox('Click here to proceed'):
            st.success('Data Filtered Successfully !')
            st.write(df_orig.shape)
            dataset_flag = 1

    else:
        dataset_flag = 0

    if dataset_flag == 1:
        ################################################################
        # st.write(df_orig.shape)
        with st.expander('Click to View Data'):
            st.write(df_orig.head(10))

        list_cols = list(df_orig.columns)
        list_cols.sort()

        with st.expander('Click to View Columns'):
            st.write(df_orig.columns)

        flag_proceed = True
        #################################################################
        ## Passing Variable to Other Pages

        st.session_state['df_orig']      = df_orig
        st.session_state['dataset_flag'] = dataset_flag
        st.session_state['dataset_path'] = dataset_path
        st.session_state['flag_proceed'] = flag_proceed
        st.success('Please Proceed for Career Visualization Step!')
        ##############################################################################
    else:
        flag_proceed=False
        st.session_state['flag_proceed'] = flag_proceed
################################################################
elif home_selected == 'Career Visualization':
    ###################################################
    ## Getting Sesssion Variables
    try:
        df_orig      = st.session_state['df_orig']
        dataset_flag = st.session_state['dataset_flag']
        dataset_path = st.session_state['dataset_path']
        flag_proceed = st.session_state['flag_proceed']
        flag_error = False
    except Exception as e:
        st.error('Please do Data Import first!')
        flag_error   = True
        dataset_flag = False
        flag_proceed = False
    #################################################################
    if ((dataset_flag) & (flag_proceed)):
            list_cols = list(df_orig.columns)

            # col_analyze = st.selectbox('Select Column to Analyze', list_cols)

            # if st.checkbox('Click to Proceed'):
            if True:
                # st.write(df_orig)

                if not df_orig.empty:
                    # st.write(df_orig.shape)

                    col_inp_job_start = 'Job Profile - Current'
                    col_inp_job_end   = 'Job Profile - Proposed'

                    sel_inp_job_options_start = list(set(list(df_orig[col_inp_job_start])))
                    sel_inp_job_options_start.sort()

                    sel_inp_job_options_end = list(set(list(df_orig[col_inp_job_end])))
                    sel_inp_job_options_end.sort()

                    ################################################################
                    opt_selected = option_menu(None,
                                                ['Current Job',
                                                 'Proposed Job',
                                                 ],
                                                icons=['graph-up-arrow', 'graph-down-arrow'],
                                                ## icons from website: https://icons.getbootstrap.com/
                                                menu_icon="cast", default_index=0, orientation="horizontal")
                    ################################################################
                    col1, col2 = st.columns(2)
                    sel_inp_job_start = []
                    sel_inp_job_end   = []

                    df_new = pd.DataFrame()

                    col_show = st.columns(2)
                    thresh_val = col_show[0].slider('Select the Min Probability Threshold', 0, 100, 16)

                    custom_sort_order = ['20', '30', '40', '50', '60', '70', '80', '90', 'EL1', 'EL2', 'EL3', 'EL4',
                                         'EXCO']

                    with col_show[1]:
                        promotion_flag = tog.st_toggle_switch(label='Only Show Promotions',
                                                                default_value=True,
                                                                label_after=True,
                                                                inactive_color='#D3D3D3',
                                                                active_color="#11567f",
                                                                track_color="#29B5E8"
                                                                )
                    df_orig = df_orig[df_orig['Job Profile - Proposed Probability'].astype(float) >= (thresh_val / 100.0)].copy()
                    df_orig['Job Profile - Current Grade'] = \
                    df_orig['Job Profile - Current'].str.replace(' \(inactive\)', '').str.split(' ').str[-1]
                    df_orig['Job Profile - Proposed Grade'] = \
                    df_orig['Job Profile - Proposed'].str.replace(' \(inactive\)', '').str.split(' ').str[-1]

                    df_orig['Job Profile - Current Grade'] = np.where(
                        df_orig['Job Profile - Current Grade'].isin(custom_sort_order),
                        df_orig['Job Profile - Current Grade'], 'Unknown')
                    df_orig['Job Profile - Proposed Grade'] = np.where(
                        df_orig['Job Profile - Proposed Grade'].isin(custom_sort_order),
                        df_orig['Job Profile - Proposed Grade'], 'Unknown')

                    # Define a function to check for promotion
                    def check_promotion(row):
                        current_grade = str(row['Job Profile - Current Grade'])
                        proposed_grade = str(row['Job Profile - Proposed Grade'])

                        if current_grade not in custom_sort_order or proposed_grade not in custom_sort_order:
                            return 'Unknown'

                        current_index = custom_sort_order.index(current_grade)
                        proposed_index = custom_sort_order.index(proposed_grade)

                        if current_index < proposed_index:
                            return 'Promotion'
                        elif current_index == proposed_index:
                            return 'Same Grade'
                        else:
                            return 'Demotion'


                    # Apply the function to the DataFrame
                    df_orig['Promotion_Status'] = df_orig.apply(check_promotion, axis=1)

                    # st.write(custom_sort_order)
                    # st.write(df_orig)

                    if promotion_flag:
                        st.info('Only Promotions displayed!')
                        df_orig = df_orig[df_orig['Promotion_Status'].isin(['Promotion', 'Same Grade'])].copy()


                    if opt_selected == 'Current Job':
                        col_sel   = col1
                        col_unsel = col2
                        sel_inp_job_start = col_sel.selectbox('Select Original Job',
                                                            sel_inp_job_options_start)#,default='Head of Audit 80')
                        sel_inp_job_start=[sel_inp_job_start]
                        # st.write(sel_inp_job_start)
                        #####################
                        df_test = df_orig[((df_orig[col_inp_job_start].isin(sel_inp_job_start)))].copy()
                        # st.write(df_test.shape)
                        sel_inp_job_options_start2 = list(set(list(df_orig[((df_orig[col_inp_job_start].isin(sel_inp_job_start)))
                                                                           ][col_inp_job_end])))
                        sel_inp_job_options_start2.sort()
                        # st.write(sel_inp_job_options_start2)

                        sel_inp_job_start2 = col_sel.selectbox('Select Next Job 1',
                                                              ['All'] + sel_inp_job_options_start2)  # ,default='Head of Audit 80')
                        sel_inp_job_start2 = [sel_inp_job_start2]
                        if sel_inp_job_start2[0] == 'All':
                            sel_inp_job_start2 = sel_inp_job_options_start2
                        # st.write(sel_inp_job_start2)
                        #####################
                        df_test = pd.concat([df_test,df_orig[((df_orig[col_inp_job_start].isin(sel_inp_job_start2)))]], axis=0, ignore_index=True)
                        # st.write(df_test.shape)
                        sel_inp_job_options_start3 = list(
                            set(list(df_orig[((df_orig[col_inp_job_start].isin(sel_inp_job_start2)))
                                     ][col_inp_job_end])))
                        sel_inp_job_options_start3.sort()
                        # st.write(sel_inp_job_options_start2)

                        sel_inp_job_start3 = col_sel.selectbox('Select Next Job 2',
                                                               ['All'] + sel_inp_job_options_start3)  # ,default='Head of Audit 80')
                        sel_inp_job_start3 = [sel_inp_job_start3]
                        if sel_inp_job_start3[0] == 'All':
                            sel_inp_job_start3 = sel_inp_job_options_start3
                        # st.write(sel_inp_job_start2)
                        #####################
                        df_test = pd.concat([df_test, df_orig[((df_orig[col_inp_job_start].isin(sel_inp_job_start3)))]],
                                            axis=0, ignore_index=True)
                        # st.write(df_test.shape)
                        sel_inp_job_options_start4 = list(
                            set(list(df_orig[((df_orig[col_inp_job_start].isin(sel_inp_job_start3)))
                                     ][col_inp_job_end])))
                        sel_inp_job_options_start4.sort()

                        sel_inp_job_start4 = col_sel.selectbox('Select Next Job 3',
                                                               ['All'] + sel_inp_job_options_start4)  # ,default='Head of Audit 80')
                        sel_inp_job_start4 = [sel_inp_job_start4]
                        if sel_inp_job_start4[0] == 'All':
                            sel_inp_job_start4 = sel_inp_job_options_start4
                        #####################
                        df_test = pd.concat([df_test, df_orig[((df_orig[col_inp_job_start].isin(sel_inp_job_start4)))]],
                                            axis=0, ignore_index=True)
                        # st.write(df_test.shape)
                        sel_inp_job_options_start5 = list(
                            set(list(df_orig[((df_orig[col_inp_job_start].isin(sel_inp_job_start4)))
                                     ][col_inp_job_end])))
                        sel_inp_job_options_start5.sort()

                        sel_inp_job_start5 = col_sel.selectbox('Select Next Job 4',
                                                               ['All'] + sel_inp_job_options_start5)  # ,default='Head of Audit 80')
                        sel_inp_job_start5 = [sel_inp_job_start5]
                        if sel_inp_job_start5[0] == 'All':
                            sel_inp_job_start5 = sel_inp_job_options_start5
                        #####################
                        df_test = pd.concat([df_test, df_orig[((df_orig[col_inp_job_start].isin(sel_inp_job_start5)))]],
                                            axis=0, ignore_index=True)
                        # st.write(df_test.shape)
                        sel_inp_job_options_start6 = list(
                            set(list(df_orig[((df_orig[col_inp_job_start].isin(sel_inp_job_start5)))
                                     ][col_inp_job_end])))
                        sel_inp_job_options_start6.sort()

                        sel_inp_job_start6 = col_sel.selectbox('Select Next Job 5',
                                                               ['All'] + sel_inp_job_options_start6)  # ,default='Head of Audit 80')
                        sel_inp_job_start6 = [sel_inp_job_start6]
                        if sel_inp_job_start6[0] == 'All':
                            sel_inp_job_start6 = sel_inp_job_options_start6
                        #####################
                        df_test = pd.concat([df_test, df_orig[((df_orig[col_inp_job_start].isin(sel_inp_job_start6)))]],
                                            axis=0, ignore_index=True)
                        # st.write(df_test.shape)
                        sel_inp_job_options_start7 = list(
                            set(list(df_orig[((df_orig[col_inp_job_start].isin(sel_inp_job_start6)))
                                     ][col_inp_job_end])))
                        sel_inp_job_options_start7.sort()

                        sel_inp_job_start7 = col_sel.selectbox('Select Next Job 6',
                                                               ['All'] + sel_inp_job_options_start7)  # ,default='Head of Audit 80')
                        sel_inp_job_start7 = [sel_inp_job_start7]
                        if sel_inp_job_start7[0] == 'All':
                            sel_inp_job_start7 = sel_inp_job_options_start7
                        #####################
                        df_test.drop_duplicates(inplace=True)
                        # st.write(df_test)

                        sel_inp_job_start = sel_inp_job_start+\
                                            sel_inp_job_start2+\
                                            sel_inp_job_start3+\
                                            sel_inp_job_start4+\
                                            sel_inp_job_start5+ \
                                            sel_inp_job_start6+ \
                                            sel_inp_job_start7
                        # st.write(sel_inp_job_start)
                        #####################
                        if len(sel_inp_job_start) > 0:
                            if sel_inp_job_start[0] == 'All':
                                sel_inp_job_start = sel_inp_job_options_start

                            # st.write(sel_inp_job_start)
                            # df_new = df_orig[df_orig[col_inp_job_start].isin(sel_inp_job_start)].copy()
                            df_new = df_test.copy()

                    elif opt_selected == 'Proposed Job':
                        col_sel   = col2
                        col_unsel = col1
                        sel_inp_job_end = col_sel.multiselect('Select Final Job',
                                                           ['All']+sel_inp_job_options_end,
                                                           default=sel_inp_job_options_end[:5])
                        # st.write(sel_inp_job_end)
                        if len(sel_inp_job_end)>0:
                            if sel_inp_job_end[0] == 'All':
                                sel_inp_job_end = sel_inp_job_options_end

                            df_new = df_orig[df_orig[col_inp_job_end].isin(sel_inp_job_end)].copy()
                            # st.write(df_new)

                    if ((df_new.shape[0]>0) & ((len(sel_inp_job_start)>0) | (len(sel_inp_job_end)>0))):
                        col_unsel.write('')
                        col_unsel.write('')

                        custom_sort_order = custom_sort_order + ['Unknown']

                        # df_new.sort_values(by='Job Profile - Proposed Grade', inplace=True)

                        # thresh_val = col_unsel.slider('Select the Min Probability Threshold', 0, 100, 16)
                        #
                        # df_new = df_new[df_new['Job Profile - Proposed Probability'].astype(float) >= (thresh_val/100.0)].copy()

                        # df_new
                        with col_unsel.expander('Click to view Data'):
                            st.write(df_new)
                            st.markdown(f"Click to download Data")
                            st.markdown(str(
                                '<button type="button">' + get_table_download_link(df_new) + '</button>'),
                                unsafe_allow_html=True)

                        ####################################################################################
                        colss = st.columns(2)
                        opt_menu = colss[0].radio('Plot Type', options=['Static', 'Dynamic'], index=1, horizontal=True)

                        if opt_menu == 'Static':
                            static_plot(data=df_new.copy(),
                                        custom_sort_order= custom_sort_order)
                        #####################################################
                        elif opt_menu == 'Dynamic':
                            interactive_plot(data=df_new.copy(), strm_col = colss[1],
                                             custom_sort_order= custom_sort_order)
                        #######################################################

                        # st.plotly_chart(fig4)
                    else:
                        st.error('No Data to show!')
                ########################
                ## Passing Variables
                st.session_state['df_orig']                 = df_orig
                st.session_state['dataset_flag']            = dataset_flag
                st.session_state['dataset_path']            = dataset_path
                # st.session_state['col_analyze_preprocess']  = col_analyze
                st.session_state['flag_proceed_preprocess'] = True
                # st.success('Please Proceed for Prefilteration  Step!')
            else:
                st.session_state['flag_proceed_preprocess'] = False
    else:
        if not flag_error:
            st.error('Please do Data Import first!')
        flag_proceed = False
        st.session_state['flag_proceed'] = False
################################################################
