# 9. Write a Python program to display the examination schedule. (extract the date from exam_st_date). Go to the editor
# exam_st_date = (11, 12, 2014)
# Sample Output : The examination will start from : 11 / 12 / 2014

exam_st_date = (25, 1, 2001)
date_list = ','.join(map(str, exam_st_date))
list = date_list.split(',')
print("The examination will start from : " + list[0] + " / " + list[1] + " / " + list[-1])

exam_st_date = (23, 8, 2000)
print( "The examination will start from : %i / %i / %i"%exam_st_date)