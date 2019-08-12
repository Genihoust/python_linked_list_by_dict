
def add_new_data_in_list(data_m, template_list_entry={'p_start': None, 'start_hash': 0,'p_end': None, 'end_hash': 0, 'count': 0}):
		
	new_template_m = {'p_next': None, 'p_forward': None, 'hash': 0, 'data': []}
	new_template_m['data'] = [data_m]
		
	if template_list_entry['count'] == 0:
		new_template_m['hash'] = 0
		template_list_entry['p_end'] = new_template_m
		template_list_entry['p_start'] = new_template_m
		template_list_entry['end_hash'] = 0
		template_list_entry['start_hash'] = 0
		
	else:
		new_template_m['hash'] = template_list_entry['p_end']['hash'] + 1
		new_template_m['p_forward'] = template_list_entry['p_end']

		new_template_m['p_forward']['p_next'] = new_template_m
		
		template_list_entry['end_hash'] = new_template_m['hash']
		template_list_entry['p_end'] = new_template_m
	
	template_list_entry['count'] = template_list_entry['count'] + 1		
	
	return template_list_entry, new_template_m


def call_back_traversing_data(last_result, data_m, arg_m):
	print(data_m)
	return last_result


def traversing_data_in_list(template_list_entry, call_back_traversing_data, arg_m=[],key_hash=-1):
	
	p_start = template_list_entry['p_start']
	if p_start == None:
		return 
	tmp_list_m = p_start
	is_end = False
	last_result = None
	while True:
	
		if is_end:
			break
		
		if key_hash == -1:
			last_result = call_back_traversing_data(last_result, tmp_list_m['data'], arg_m)
		else:
			if tmp_list_m['hash'] == key_hash:
				last_result = call_back_traversing_data(last_result, tmp_list_m['data'], arg_m)		
	
		if template_list_entry['end_hash'] == tmp_list_m['hash']:
			is_end = True
			
		if tmp_list_m['p_next'] == None:
			is_end = True
		
		tmp_list_m = tmp_list_m['p_next']
	
	return last_result


def echo_all_data_in_list(template_list_entry):
	traversing_data_in_list(template_list_entry, call_back_traversing_data)
	

def call_back_modify_data(last_result, data_m, arg_m):
	data_m[0] = arg_m
	return last_result


def modify_data_in_list(template_list_entry, key_hash, data_m):
	traversing_data_in_list(template_list_entry, call_back_modify_data, data_m, key_hash)
	

def delete_data_in_list(template_list_entry, key_hash):
	
	if template_list_entry['count'] <= 0:
		template_list_entry['count'] = 0
		return 
		
	p_start = template_list_entry['p_start']
	tmp_list_m = p_start
	is_end = False
	last_result = None
	while True:
	
		if is_end:
			break
		
		if tmp_list_m['hash'] == key_hash:
			if tmp_list_m['p_forward'] != None:
				tmp_list_m['p_forward']['p_next'] = tmp_list_m['p_next']
			
			if tmp_list_m['p_next'] != None:
				tmp_list_m['p_next']['p_forward'] = tmp_list_m['p_forward']
			
			template_list_entry['count'] = template_list_entry['count'] - 1
			
			del tmp_list_m
			
			if template_list_entry['count'] == 0:
				template_list_entry['p_start'] = None 
				template_list_entry['p_end'] = None
				template_list_entry['p_start'] = None
				template_list_entry['end_hash'] = 0
				template_list_entry['start_hash'] = 0
		
			break
		
		if template_list_entry['end_hash'] == tmp_list_m['hash']:
			is_end = True
			
		if tmp_list_m['p_next'] == None:
			is_end = True
		
		tmp_list_m = tmp_list_m['p_next']
	
	return 


_template_list_entry_, new_list = add_new_data_in_list({'1': 1})

_template_list_entry_, new_list = add_new_data_in_list({'2': 2}, template_list_entry=_template_list_entry_)

_template_list_entry_, new_list = add_new_data_in_list({'3': 3}, template_list_entry=_template_list_entry_)

modify_data_in_list(_template_list_entry_, 1, {'modify': 1})

echo_all_data_in_list(_template_list_entry_)

print("-----")
delete_data_in_list(_template_list_entry_, 2)

echo_all_data_in_list(_template_list_entry_)

print("-----")
delete_data_in_list(_template_list_entry_, 1)
echo_all_data_in_list(_template_list_entry_)

print("-----")
delete_data_in_list(_template_list_entry_, 0)
echo_all_data_in_list(_template_list_entry_)

print(_template_list_entry_)










		
	