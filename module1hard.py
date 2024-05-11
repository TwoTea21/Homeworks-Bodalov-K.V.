from statistics import fmean

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

gr = grades
st = (sorted(set(students)))

gr[0], gr[1], gr[2], gr[3], gr[4], = fmean(gr[0]), fmean(gr[1]), fmean(gr[2]), fmean(gr[3]), fmean(gr[4])


gr_st = {st[0]: gr[0], st[1]: gr[1], st[2]: gr[2], st[3]: gr[3], st[4]: gr[4]}

print(gr_st)
