try:
	from vars import *
except:
	from py_tarif.vars import *

data = \
	{
		'wifi':
			{
				'prim':
					{
						'control-3600':
							{
								'sms-1100': all_control_wifi_dop,
								'nosms-800': all_control_wifi_dop
							},
						'guest':
							{
								'start-0/700': all_wifi_guest_dop,
								'improve-3600/1450': all_wifi_guest_dop,
								'extended-3600/1100': all_wifi_guest_dop
							}
					},
				'khab':
					{
						'control-3600':
							{
								'sms-1100': all_control_wifi_dop,
								'nosms-800': all_control_wifi_dop
							},
						'guest':
							{
								'start-0/700': all_wifi_guest_dop,
								'improve-3600/1450': all_wifi_guest_dop,
								'extended-3600/1100': all_wifi_guest_dop
							}
					},
				'sakh':
					{
						'control-3600':
							{
								'sms-1100': all_control_wifi_dop,
								'nosms-800': all_control_wifi_dop
							},
						'guest':
							{
								'start-0/700': all_wifi_guest_dop,
								'improve-3600/1450': all_wifi_guest_dop,
								'extended-3600/1100': all_wifi_guest_dop
							}
					},
				'kamch':
					{
						'control-3600':
							{
								'sms-1100': all_control_wifi_dop,
								'nosms-800': all_control_wifi_dop
							},
						'guest':
							{
								'start-0/700': all_wifi_guest_dop,
								'improve-3600/1450': all_wifi_guest_dop,
								'extended-3600/1100': all_wifi_guest_dop
							}
					},
				'amur':
					{
						'control-3600':
							{
								'sms-1100': all_control_wifi_dop,
								'nosms-800': all_control_wifi_dop
							},
						'guest':
							{
								'start-0/700': all_wifi_guest_dop,
								'improve-3600/1450': all_wifi_guest_dop,
								'extended-3600/1100': all_wifi_guest_dop
							}
					},
				'maga':
					{
						'control-3600':
							{
								'sms-1100': all_control_wifi_dop,
								'nosms-800': all_control_wifi_dop
							},
						'guest':
							{
								'start-0/700': all_wifi_guest_dop,
								'improve-3600/1450': all_wifi_guest_dop,
								'extended-3600/1100': all_wifi_guest_dop
							}
					},
				'sakhtel':
					{
						'control-3600':
							{
								'sms-1100': all_control_wifi_dop,
								'nosms-800': all_control_wifi_dop
							},
						'guest':
							{
								'start-0/700': all_wifi_guest_dop,
								'improve-3600/1450': all_wifi_guest_dop,
								'extended-3600/1100': all_wifi_guest_dop
							}
					}
			},
		'internet':
			internet_tariff,
		'wats':
			{
				'prim': wats_tariff,
				'khab': wats_tariff,
				'sakh': wats_tariff,
				'kamch': wats_tariff,
				'amur': wats_tariff,
				'maga': wats_tariff,
				'sakhtel': wats_tariff
			},
		'vn':
			{
				'prim': vn_tariff,
				'khab': vn_tariff,
				'sakh': vn_tariff,
				'kamch': vn_tariff,
				'amur': vn_tariff,
				'maga': vn_tariff,
				'sakhtel': vn_tariff
			},
		'iptv/hot':
			{
				'prim': iptv_hot_tariff,
				'khab': iptv_hot_tariff,
				'sakh': iptv_hot_tariff,
				'kamch': iptv_hot_tariff,
				'amur': iptv_hot_tariff,
				'maga': iptv_hot_tariff,
				'sakhtel': iptv_hot_tariff
			},
		'iptv':
			{
				'prim': {'public': public_iptv, 'private': private_iptv},
				'khab': {'public': public_iptv, 'private': private_iptv},
				'sakh': {'public': public_iptv, 'private': private_iptv},
				'kamch': {'public': public_iptv, 'private': private_iptv},
				'amur': {'public': public_iptv, 'private': private_iptv},
				'maga': {'public': public_iptv, 'private': private_iptv},
				'sakhtel': {'public': public_iptv, 'private': private_iptv},
			},
	}