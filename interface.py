import tkinter as tk
IntVar = tk.IntVar

from candidate import gen_candidates


window = tk.Tk()
window.title("Prime Number Search")
##window.configure(bg='black')

#main window
window.rowconfigure(0, minsize=0, weight=1)
window.columnconfigure(0, minsize=0, weight=1)

#establish each of the frames to be used
fr_state = tk.Frame(window)
fr_search = tk.Frame(window)
fr_stats_overview = tk.Frame(window)
fr_stats_coarse = tk.Frame(window)
fr_stats_fine = tk.Frame(window)
fr_candidates = tk.Frame(window)
fr_file_integrity = tk.Frame(window)
fr_exit = tk.Frame(window)

#example of how to change the background on a frame to black
#however, i would have to update all the buttons and labels as well
#it would be nice if there were a way to change all windows, frames, labels, buttons, etc. at once
##fr_state.configure(bg='black')


#frame locations
fr_state.grid(row=0, column=0, sticky='nwe')
fr_search.grid(row=1, column=0, sticky='nwe')
fr_stats_overview.grid(row=2, column=0, sticky='nwe')
fr_stats_coarse.grid(row=3, column=0, sticky='nwe')
fr_stats_fine.grid(row=4, column=0, sticky='nwe')
fr_candidates.grid(row=5, column=0, sticky='nwe')
fr_file_integrity.grid(row=6, column=0, sticky='nwe')
fr_exit.grid(row=7, column=0, sticky='nwe')


#text formats
text_14ub = ('Courier New','14','underline','bold')
text_10 = ('Courier New','10')
text_12b = ('Courier New','12','bold')
text_11b = ('Courier New','11','bold')


underscore_text= '____________________________________'
time_format = 'YYYY-MM-DD:HH-mm-ss'
time_default = '____-__-__:__-__-__'
default_number = '####'
default_percent = '##.##'

####
####State
####

#Widgets for state frame
lbl_state = tk.Label(fr_state, text='State', font=text_14ub)
lbl_state_found = tk.Label(fr_state, text='Found All Primes : ', font=text_10)
lbl_state_found_v = tk.Label(fr_state, text=underscore_text, font=text_10)
lbl_state_candidates = tk.Label(fr_state, text='Candidates Ready: ', font=text_10)
lbl_state_candidates_v = tk.Label(fr_state, text=underscore_text, font=text_10)
lbl_state_approx_left = tk.Label(fr_state, text='Approx. Candidates Left: ', font=text_10)
lbl_state_approx_left_v = tk.Label(fr_state, text=underscore_text, font=text_10)

#and their locations.
lbl_state.grid(row=0, column=0, sticky='w')
lbl_state_found.grid(row=1, column=0, sticky='w')
lbl_state_found_v.grid(row=1, column=1, sticky='w')
lbl_state_candidates.grid(row=2, column=0, sticky='w')
lbl_state_candidates_v.grid(row=2, column=1, sticky='w')
lbl_state_approx_left.grid(row=3, column=0, sticky='w')
lbl_state_approx_left_v.grid(row=3, column=1, sticky='w')

####
####Search
####
def find_next():
    cbx_keep_finding.deselect()
    cbx_find.toggle()
    if cbx_find_v.get():
        gen_candidates()

def keep_finding():
    if cbx_find_v.get():
        cbx_keep_finding.toggle()

    current_time = 0
    time_limit = 100 #loops, but needs to be time based
    while cbx_find_v.get() and cbx_keep_finding_v.get() and current_time < time_limit:
        gen_candidates()
        #this is just a loop counter, but should be updated
        #to a time based counter at some point.
        current_time+=1

cbx_find_v = IntVar()
cbx_keep_finding_v = IntVar()

#Widgets for search frame
lbl_search = tk.Label(fr_search, text='Search', font=text_14ub)
btn_find = tk.Button(fr_search, text='Find\nNext', font=text_10, command=find_next, width=7)
cbx_find = tk.Checkbutton(fr_search, variable=cbx_find_v, font=text_10, onvalue=1, offvalue=0, command=find_next)
btn_keep_finding = tk.Button(fr_search, text='Keep\nFinding', font=text_10, command=keep_finding, width=7)
cbx_keep_finding = tk.Checkbutton(fr_search, variable=cbx_keep_finding_v, font=text_10, onvalue=1, offvalue=0, command=keep_finding)

#and their locations.
lbl_search.grid(row=0, column=0, sticky='w')
btn_find.grid(row=1, column=0)
cbx_find.grid(row=1, column=1, sticky='w')
btn_keep_finding.grid(row=1, column=2)
cbx_keep_finding.grid(row=1, column=3, sticky='w')



####
####Stats - Overview
####

def my_next_function():
    print('potato')

#Widgets for the overview frame
lbl_overview = tk.Label(fr_stats_overview, text='Stats: Overview', font=text_14ub)
lbl_len_candidate = tk.Label(fr_stats_overview, text='Length Current\n(digits)', font=text_12b)
lbl_len_candidate_v = tk.Label(fr_stats_overview, text=default_number, font=text_10)

lbl_time_current_candidate = tk.Label(fr_stats_overview, text='Time Current', font=text_12b)
lbl_time_current_candidate_header = tk.Label(fr_stats_overview, text=time_format, font=text_10)
lbl_time_current_candidate_v = tk.Label(fr_stats_overview, text=time_default, font=text_10)

lbl_time_previous = tk.Label(fr_stats_overview, text='Highest Previous', font=text_12b)
lbl_time_previous_header = tk.Label(fr_stats_overview, text=time_format, font=text_10)
lbl_time_previous_v = tk.Label(fr_stats_overview, text=time_default, font=text_10)

#and their locations
lbl_overview.grid(row=0, column=0, sticky='sw')
lbl_len_candidate.grid(row=1, column=0, rowspan=2, sticky='sw')
lbl_len_candidate_v.grid(row=3, column=0, sticky='n')
lbl_time_current_candidate.grid(row=1, column=1, sticky='sw')
lbl_time_current_candidate_header.grid(row=2, column=1, sticky='se', ipadx=10)
lbl_time_current_candidate_v.grid(row=3, column=1, sticky='ne', ipadx=10)
lbl_time_previous.grid(row=1, column=2, sticky='sw')
lbl_time_previous_header.grid(row=2, column=2, sticky='se', ipadx=10)
lbl_time_previous_v.grid(row=3, column=2, sticky='ne', ipadx=10)


####
####Stats - Coarse Progress
####

#Widgets for the coarse progress frame
lbl_coarse = tk.Label(fr_stats_coarse, text='Stats: Coarse Progress', font=text_14ub)
lbl_length_divisor = tk.Label(fr_stats_coarse, text='Length Divisor\n(digits)', font=text_12b)
lbl_length_divisor_v = tk.Label(fr_stats_coarse, text=default_number, font=text_10)
lbl_length_highest_divisor = tk.Label(fr_stats_coarse, text='Length Highest Divisor\n(digits)', font=text_12b)
lbl_length_highest_divisor_v = tk.Label(fr_stats_coarse, text=default_number, font=text_10)
lbl_percent_current_highest_divisor = tk.Label(fr_stats_coarse, text='Current/Highest Divisor\n(%)', font=text_12b)
lbl_percent_current_highest_divisor_v = tk.Label(fr_stats_coarse, text=default_percent, font=text_10)

##and their locations
lbl_coarse.grid(row=0, column=0, sticky='w')
lbl_length_divisor.grid(row=1, column=0)
lbl_length_divisor_v.grid(row=2, column=0)
lbl_length_highest_divisor.grid(row=1, column=1)
lbl_length_highest_divisor_v.grid(row=2, column=1)
lbl_percent_current_highest_divisor.grid(row=1, column=2)
lbl_percent_current_highest_divisor_v.grid(row=2, column=2)



####
####Stats - Fine Progress
####

#Widgets for the fine progress frame
lbl_progress = tk.Label(fr_stats_fine, text='Stats: Fine Progress', font=text_14ub)
lbl_time_current_divisor = tk.Label(fr_stats_fine, text='Time Current Divisor', font=text_12b)
lbl_time_current_divisor_header = tk.Label(fr_stats_fine, text=time_format, font=text_10)
lbl_time_current_divisor_v = tk.Label(fr_stats_fine, text=time_default, font=text_10)

lbl_length_quotient = tk.Label(fr_stats_fine, text='Length Quotient\n(digits)', font=text_12b)
lbl_length_quotient_v = tk.Label(fr_stats_fine, text=default_number, font=text_10)

lbl_max_length_quotient = tk.Label(fr_stats_fine, text='Max Length Quotient\n(digits)', font=text_12b)
lbl_max_length_quotient_v = tk.Label(fr_stats_fine, text=default_number, font=text_10)

lbl_percent_completed = tk.Label(fr_stats_fine, text='Percent Completed\n(%)', font=text_12b)
lbl_percent_completed_v = tk.Label(fr_stats_fine, text=default_percent, font=text_10)

##and their locations
lbl_progress.grid(row=0, column=0, sticky='w')
lbl_time_current_divisor.grid(row=1, column=0, sticky='sw')
lbl_time_current_divisor_header.grid(row=2, column=0, sticky='e')
lbl_time_current_divisor_v.grid(row=3, column=0, sticky='e')

lbl_length_quotient.grid(row=1, column=1, sticky='w', rowspan=2)
lbl_length_quotient_v.grid(row=3, column=1)

lbl_max_length_quotient.grid(row=1, column=2, sticky='', rowspan=2)
lbl_max_length_quotient_v.grid(row=3, column=2)

lbl_percent_completed.grid(row=1, column=3, sticky='w', rowspan=2)
lbl_percent_completed_v.grid(row=3, column=3)




# not really needed at this stage
# when the folder structure updates to the next iteration
# this will be good to have

######
######Candidates
######
##
##def get_candidates():
##    cbx_get_candidates.toggle()
##    if cbx_get_candidates_v.get():
##        print('Get Candidates')
##
##cbx_get_candidates_v = IntVar()
##
###Widgets for the candidates frame
##lbl_candidates = tk.Label(fr_candidates, text='Candidates', font=text_14ub)
##btn_get_candidates = tk.Button(fr_candidates, text='Get Candidates', font=text_10, command=get_candidates, width=15)
##cbx_get_candidates = tk.Checkbutton(fr_candidates, variable=cbx_get_candidates_v, font=text_10, onvalue=1, offvalue=0, command=get_candidates)
##
###and their locations
##lbl_candidates.grid(row=0, column=0, sticky='w')
##btn_get_candidates.grid(row=1, column=0, sticky='e')
##cbx_get_candidates.grid(row=1, column=1, sticky='w')



####
####File Integrity
####

def check_files():
    cbx_check_files.toggle()
    if cbx_check_files_v.get():
        print('Check Files')

cbx_check_files_v = IntVar()

#Widgets for the file integrity frame
lbl_file_integrity = tk.Label(fr_file_integrity, text='File Integrity', font=text_14ub)
btn_check_files = tk.Button(fr_file_integrity, text='Check Files', font=text_10, command=check_files, width=15)
cbx_check_files = tk.Checkbutton(fr_file_integrity, variable=cbx_check_files_v, font=text_10, onvalue=1, offvalue=0, command=check_files)

#and their locations
lbl_file_integrity.grid(row=0, column=0, sticky='w')
btn_check_files.grid(row=1, column=0, sticky='e')
cbx_check_files.grid(row=1, column=1, sticky='w')




####
####Close
####
def close():
    cbx_close_now.deselect()
    cbx_close.toggle()
    if cbx_close_v.get() and not cbx_close_now_v.get():
        #if the close field is checked, and the close now is not checked, then close at the end of the next iteration
        cbx_keep_finding.deselect()
        cbx_find.deselect()
        print('Close safely')
        # i'm not sure which one to use here
        # it doesn't seem to matter, as I can't click them when
        # the program is running anyway
##        window.quit()
##        window.destroy()

def close_now():
    cbx_close_now.toggle()

    #exit immediately
    if cbx_close_now_v.get():
        print('Close now')

cbx_close_v = IntVar()
cbx_close_now_v = IntVar()

#Widgets for close frame
lbl_close = tk.Label(fr_exit, text='Close', font=text_14ub)
btn_close = tk.Button(fr_exit, text='Close\nSafely', font=text_10, command=close, width=7)
cbx_close = tk.Checkbutton(fr_exit, variable=cbx_close_v)
btn_close_now = tk.Button(fr_exit, text='Lose\nWork', font=text_10, command=close_now, width=7)
cbx_close_now = tk.Checkbutton(fr_exit, variable=cbx_close_now_v)

#and their locations.
lbl_close.grid(row=0, column=0, sticky='w')
btn_close.grid(row=1, column=0)
cbx_close.grid(row=1, column=1, sticky='w')
btn_close_now.grid(row=1, column=2)
cbx_close_now.grid(row=1, column=3, sticky='w')




window.mainloop()
