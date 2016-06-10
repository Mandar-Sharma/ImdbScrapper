list = [u'/title/tt2277860/news?ref_=tt_nwr_sm',
 u'/lists/tt2277860?ref_=tt_rls_sm',
 u'/poll/?ref_=tt_po_sm',
 u'fullcredits?ref_=tt_cl_sm#cast',
 u'/title/tt2277860/reviews-enter?ref_=tt_urv',
 u'/title/tt2277860/board/?ref_=tt_bd_sm']

for thisthing in list:
	if thisthing.startswith('fullcredits'):
		index_this = list.index(thisthing)
print index_this