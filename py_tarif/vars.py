all_control_wifi_dop = \
    {
        'dop': {
            'filter-600': 'dop-next',
            'block-50': 'dop-next',
            'radar':
                {
                    'once/3600': {'1': 3000, '3': 2600, '5': 2300, '10': 1900},
                    '6m/2400': {'1': 2600, '3': 2300, '5': 2000, '10': 1700},
                    '12m/1': {'1': 2300, '3': 2000, '5': 1700, '10': 1400}
                },
            'wifi/pass': 'dop-fin'
        }
    }

all_wifi_guest_dop = \
    {
        'speed': {'prim': {'10': 6600, '20': 8400, '30': 10800, '50': 18000, '80': 24000,
                           '100': 30000},
                  'khab': {'10': 6100, '20': 9050, '30': 12000, '50': 16950, '80': 25050,
                           '100': 32800},
                  'sakh': {'10': 8050, '20': 15950, '30': 23850, '50': 39550, '80': 59400,
                           '100': 76100},
                  'kamch': {'10': 21600, '20': 29400, '30': 38400, '50': 64200, '80': 78000,
                            '100': 97200},
                  'amur': {'10': 7200, '20': 10550, '30': 13050, '50': 19650, '80': 28950,
                           '100': 38900},
                  'maga': {'10': 17050, '20': 24600, '30': 29100, '50': 38350, '80': 46200,
                           '100': 57550},
                  'sakhtel': {'10': 13200, '20': 17050, '30': 22600, '50': 32550, '80': 46150,
                              '100': 59700}
                  },

        'dop':
            {
                'filter-600': 'dop-next',
                'block-50': 'dop-next',
                'radar':
                    {
                        'once/3600': {'1': 3000, '3': 2600, '5': 2300, '10': 1900},
                        '6m/2400': {'1': 2600, '3': 2300, '5': 2000, '10': 1700},
                        '12m/1': {'1': 2300, '3': 2000, '5': 1700, '10': 1400}
                    },
                'adv':
                    {
                        'access': 3600, '12m': 1800, 'extended': 1050,
                    },
                'wifi/pass': 'dop-fin'

            }
    }

public_iptv = \
    {
        'kostyl':
            {
                'sfera/other': 400, 'sfera+/other': 750, 'dvb/sfera/nodop': 300,
                'sfera': 600, 'sfera+': 1200, 'kids': 400, 'kids+': 800, 'dvb/lite': 300,
                'dvb/sfera': 600, 'dvb/sfera+': 1200, 'dvb/kids': 400, 'dvb/kids+': 800
            },
        'main':
            {
                'sokr/stb':
                    {
                        'kids': 400, 'kids+': 800, 'dvb/sfera': 600, 'dvb/sfera+': 1200
                    },
                'sokr/dvb':
                    {
                        'kids': 400, 'dvb/sfera': 600, 'dvb/sfera+': 1200, 'dvb/sfera/nodop': 300
                    },
                'sokr/ott':
                    {
                        'sfera/other': 400, 'sfera+/other': 750,
                    },
                'sokr/sm':
                    {
                        'kids': 400, 'kids+': 800, 'dvb/sfera': 600, 'dvb/sfera+': 1200
                    }
            },
        'dopchannel':
            {
                'khlprime': 149,
                'match': 100,
                'supermatch': 450,
                'china': 360,
                'smart':
                    {
                        'sm.kids': 400,
                        'sm.kids+': 800,
                        'sm.sfera': 600,
                        'sm.sfera+': 1200,
                        'sm.sfera/other': 400,
                        'sm.sfera+/other': 750,
                    },
                # 'smart':
                #     {
                #         'sferaSM3': 350,
                #         'sferaSM6': 650,
                #         'sferaSM12': 1250,
                #         'basekids': 450,
                #         'basekids+': 900
                #     },
                'pass/dopchannel': 'dopchannel-fin'
            },
        'dop':
            {
                'videomuz':
                    {
                        1: 100, 2: 150, 3: 200, 4: 250, 5: 300,
                        6: 350, 7: 400, 8: 450, 9: 500, 10: 750, 11: 1000
                    },
                'content/contr': '-',
                'adv/konst': 220,
                'iptv/block': 20,
                'pass': 'dop-fin'
            }

    }

private_iptv = \
    {
        'kostyl':
            {
                'office': 600, 'office+': 1000,
                'dvb/office/nodop': 250, 'office/other': 400, 'office+/other': 750,
                'office/sm': 600, 'office+/sm': 1000,
                'office/other/sm': 400, 'office+/other/sm': 750,
                'sfera/other': 400, 'sfera+/other': 750,
            },
        'main':
            {
                'sokr/office':
                    {
                        'office': 600, 'office+': 1000, 'office/sm': 600, 'office+/sm': 1000,
                        'office/other/sm': 400, 'office+/other/sm': 750,
                    },
                'sokr/ott':
                    {
                        'sfera/other': 400, 'sfera+/other': 750,
                    },
                'sokr/dvb':
                    {
                        'office': 600, 'dvb/office/nodop': 250, 'office+': 1000,
                    },
            },
        'dopchannel':
            {
                'match': 100,
                'supermatch': 450,
                'adult+': 750,
                'china': 360,
                'pass/dopchannel': 'dopchannel-fin'
            },
        'dop':
            {
                'content/contr': 450,
                'adv/konst': 220,
                'iptv/block': 20,
                'pass': 'dop-fin'
            }
    }

wats_tariff_cat =\
    {
        'platinum-100000': 100000, 'gold-40000': 40000,
        'silver-15000': 15000, 'bronze-5000': 5000, 'nocat': 'in/abon'
    }

wats_tariff = \
    {
        'busyness/virt':
            {
                'bus/st':
                    {
                        'numbCat': wats_tariff_cat,
                        'speed':
                            {
                                'prim': {'do5': 915, 'more5user': '915+169.5*(n-5)'},
                                'khab': {'do5': 915, 'more5user': '915+169.5*(n-5)'},
                                'sakh': {'do5': 1119, 'more5user': '1119+169.5*(n-5)'},
                                'kamch': {'do5': 1119, 'more5user': '1119+169.5*(n-5)'},
                                'amur': {'do5': 915, 'more5user': '915+169.5*(n-5)'},
                                'maga': {'do5': 1119, 'more5user': '1119+169.5*(n-5)'},
                                'sakhtel': {'do5': 1525, 'more5user': '1525+169.5*(n-5)'}
                            },
                        'dop':
                            {
                                'vid/back-500': 500,
                                'virt/contact/2-600': 600,
                                'virt/contact/dop-120': 120,
                                'other/crm-508': 508,
                                'pass/wats': 'dop-fin'
                            }
                    },
                'bus/unlim':
                    {
                        'numbCat': wats_tariff_cat,
                        'speed':
                            {
                                'prim': {'do5': 2542, 'more5user': '2542+254.24*(n-5)'},
                                'khab': {'do5': 1627, 'more5user': '1627+211.86*(n-5)'},
                                'sakh': {'do5': 1932, 'more5user': '1932+254.24*(n-5)'},
                                'kamch': {'do5': 1932, 'more5user': '1932+254.24*(n-5)'},
                                'amur': {'do5': 1627, 'more5user': '1627+211.86*(n-5)'},
                                'maga': {'do5': 2542, 'more5user': '2542+254.25*(n-5)'},
                                'sakhtel': {'do5': 3050, 'more5user': '3050+381.36*(n-5)'}
                            },
                        'dop':
                            {
                                'vid/back-500': 500,
                                'virt/contact/2-600': 600,
                                'virt/contact/dop-120': 120,
                                'other/crm-508': 508,
                                'pass/wats': 'dop-fin'
                            }
                    },
                'virt/st':
                    {
                        'numbCat': wats_tariff_cat,
                        'speed':
                            {
                                'prim': {'1user': 458, '23user': '458+169.5*(n-1)'},
                                'khab': {'1user': 458, '23user': '458+169.5*(n-1)'},
                                'sakh': {'1user': 458, '23user': '458+169.5*(n-1)'},
                                'kamch': {'1user': 458, '23user': '458+169.5*(n-1)'},
                                'amur': {'1user': 458, '23user': '458+169.5*(n-1)'},
                                'maga': {'1user': 458, '23user': '458+169.5*(n-1)'},
                                'sakhtel': {'1user': 458, '23user': '458+169.5*(n-1)'}
                            },
                        'dop':
                            {
                                'vid/back-500': 500,
                                'virt/contact/2-600': 600,
                                'virt/contact/dop-120': 120,
                                'other/crm-508': 508,
                                'pass/wats': 'dop-fin'
                            }
                    },
                'virt/unlim':
                    {
                        'numbCat': wats_tariff_cat,
                        'speed':
                            {
                                'prim': {'1user': 864, '23user': '861.41+508.47*(n-1)'},
                                'khab': {'1user': 610, '23user': '610.16+338.98*(n-1)'},
                                'sakh': {'1user': 661, '23user': '661.02+381.36*(n-1)'},
                                'kamch': {'1user': 458, '23user': '458+169.5*(n-1)'},
                                'amur': {'1user': 610, '23user': '610.16+338.98*(n-1)'},
                                'maga': {'1user': 864, '23user': '861.41+508.47*(n-1)'},
                                'sakhtel': {'1user': 864, '23user': '861.41+508.47*(n-1)'}
                            },
                        'dop':
                            {
                                'vid/back-500': 500,
                                'virt/contact/2-600': 600,
                                'virt/contact/dop-120': 120,
                                'other/crm-508': 508,
                                'pass/wats': 'dop-fin'
                            }
                    },
                'bus/korp20':
                    {
                        'numbCat': wats_tariff_cat,
                        'speed':
                            {
                                'prim': {'20user': 15661, 'more20User': '15661.02+652.54*(n-20)'},
                                'khab': {'20user': 15661, 'more20User': '15661.02+652.54*(n-20)'},
                                'sakh': {'20user': 15661, 'more20User': '15661.02+652.54*(n-20)'},
                                'kamch': {'20user': 15661, 'more20User': '15661.02+652.54*(n-20)'},
                                'amur': {'20user': 15661, 'more20User': '15661.02+652.54*(n-20)'},
                                'maga': {'20user': 15661, 'more20User': '15661.02+652.54*(n-20)'},
                                'sakhtel': {'20user': 19220, 'more20User': '19220.34+652.54*(n-20)'}
                            },
                        'dop':
                            {
                                'vid/back-500': 500,
                                'virt/contact/2-508': 508,
                                'virt/contact/dop-102': 102,
                                'other/crm-508': 508,
                                'pass/wats': 'dop-fin'
                            }
                    },
                'bus/korp40':
                    {
                        'numbCat': wats_tariff_cat,
                        'speed':
                            {
                                'prim': {'40user': 28475, 'more40User': '28475.58+652.54*(n-40)'},
                                'khab': {'40user': 28475, 'more40User': '28475.58+652.54*(n-40)'},
                                'sakh': {'40user': 28475, 'more40User': '28475.58+652.54*(n-40)'},
                                'kamch': {'40user': 28475, 'more40User': '28475.58+652.54*(n-40)'},
                                'amur': {'40user': 28475, 'more40User': '28475.58+652.54*(n-40)'},
                                'maga': {'40user': 28475, 'more40User': '28475.58+652.54*(n-40)'},
                                'sakhtel': {'40user': 36610, 'more40User': '36640.16+800.85*(n-40)'}
                            },
                        'dop':
                            {
                                'vid/back-500': 500,
                                'virt/contact/2-508': 508,
                                'virt/contact/dop-102': 102,
                                'other/crm-508': 508,
                                'pass/wats': 'dop-fin'
                            }
                    }

            },
        'pack/min':
            {
                'speed':
                    {
                        '3r/0m-500': 500,
                        '5r/600m-1100': 1100,
                        '10r/1200m-1900': 1900,
                        '15r/3000m-4900': 4900,
                        '30r/5000m-7900': 7900

                        # '100m-400': 400,
                        # '500m-900': 900,
                        # '1000m-1600': 1600,
                        # '1500m-2350': 2350,
                        # '2000m-3000': 3000,
                        # '3000m-4400': 4400,
                        # '5000m-7100': 7100
                    },
                'dop':
                    {
                        'more/workp':
                            {
                                '3r/0m-500': 100,
                                '5r/600m-1100': 80,
                                '10r/1200m-1900': 50,
                                '15r/3000m-4900': 40,
                                '30r/5000m-7900': 30
                                # '100m-400': 80,
                                # '500m-900': 60,
                                # '1000m-1600': 40,
                                # '1500m-2350': 40,
                                # '2000m-3000': 35,
                                # '3000m-4400': 30,
                                # '5000m-7100': 25
                            },
                        'mobile/workp-100': 100,
                        'vid/back-500': 500,
                        'anal-1': 1,
                        'virt/contact/2-500': 500,
                        'virt/contact/dop-100': 100,
                        'amocrm-500': 500,
                        'other/crm-500': 500,
                        'pass/wats': 'dop-fin'
                    }
            }
    }

vn_vid_anal =\
    {
        'visCount-1080': {'0', '10', '20', '30'},
        'lenQ-1320': {'0', '10', '20', '30'},
        'faceRec-1800': {'0', '10', '20', '30'},
        'controlEmp-1080': {'0', '10', '20', '30'},
        'heatMap-960': {'0', '10', '20', '30'},
        'autoNom-3600': {'0', '10', '20', '30'},
        'leftS-1080': {'0', '10', '20', '30'},
        'pass/dv': {'pass/dop/vid'}
    }

vn_tariff =\
    {
        'vnStan':
            {
                'stan0':
                    {
                        'saveDays':
                            {
                                '0':
                                    {
                                        'saveType':
                                            {
                                                'reg': 150
                                            }
                                    },
                                '3':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 198,
                                                        '1': 240,
                                                        '1.5': 270,
                                                        '2': 312
                                                    },
                                                'actions':
                                                    {
                                                        '512': 198,
                                                        '1': 210,
                                                        '1.5': 240,
                                                        '2': 282,
                                                        '3': 330
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 168
                                                    }

                                            }
                                    },
                                '5':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 216,
                                                        '1': 288,
                                                        '1.5': 348
                                                    },
                                                'actions':
                                                    {
                                                        '512': 216,
                                                        '1': 252,
                                                        '1.5': 312,
                                                        '3': 444
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 168
                                                    }

                                            }
                                    },
                                '7':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 288,
                                                        '1': 384,
                                                        '1.5': 432,
                                                        '2': 504
                                                    },
                                                'actions':
                                                    {
                                                        '512': 288,
                                                        '1': 336,
                                                        '1.5': 384,
                                                        '2': 444,
                                                        '3': 552
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 216
                                                    }

                                            }
                                    },
                                '10':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 432,
                                                        '1': 576,
                                                        '1.5': 648
                                                    },
                                                'actions':
                                                    {
                                                        '512': 432,
                                                        '1': 504,
                                                        '1.5': 576,
                                                        '3': 720
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 324
                                                    }

                                            }
                                    },
                                '14':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 540,
                                                        '1': 720,
                                                        '1.5': 810,
                                                        '2': 870
                                                    },
                                                'actions':
                                                    {
                                                        '512': 540,
                                                        '1': 630,
                                                        '1.5': 720,
                                                        '2': 828,
                                                        '3': 942
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 405
                                                    }

                                            }
                                    },
                                '30':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 864,
                                                        '1': 1152,
                                                        '1.5': 1296,
                                                        '2': 1680
                                                    },
                                                'actions':
                                                    {
                                                        '512': 864,
                                                        '1': 1008,
                                                        '1.5': 1152,
                                                        '2': 1440,
                                                        '3': 1860
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 648
                                                    }

                                            }
                                    },
                                '45':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 1296,
                                                        '1': 1728,
                                                        '1.5': 1944
                                                    },
                                                'actions':
                                                    {
                                                        '512': 1296,
                                                        '1': 1512,
                                                        '1.5': 1728,
                                                        '3': 2700
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 972
                                                    }

                                            }
                                    },
                                '60':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 1584,
                                                        '1': 2112,
                                                        '1.5': 2376
                                                    },
                                                'actions':
                                                    {
                                                        '512': 1584,
                                                        '1': 1848,
                                                        '1.5': 2112,
                                                        '3': 3540
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 1188
                                                    }

                                            }
                                    },
                                '90':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 2304,
                                                        '1': 3072,
                                                        '1.5': 3546
                                                    },
                                                'actions':
                                                    {
                                                        '512': 5304,
                                                        '1': 2688,
                                                        '1.5': 3072,
                                                        '3': 5160
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 1728
                                                    }

                                            }
                                    },
                                '180':
                                    {
                                        'saveType':
                                            {
                                                'actions':
                                                    {
                                                        '1.5': 7200
                                                    }

                                            }
                                    },

                            },
                        'dop':
                            {
                                'smsPack':
                                    {
                                        '100/30': 120,
                                        '500/90': 600,
                                        '1000/180': 1200,
                                        '5000/365': 6000
                                    },
                                'vidAnal':
                                    {
                                        'visCount-1080': {'0', '10', '20', '30'},
                                        'lenQ-1320': {'0', '10', '20', '30'},
                                        'faceRec-1800': {'0', '10', '20', '30'},
                                        'controlEmp-1080': {'0', '10', '20', '30'},
                                        'heatMap-960': {'0', '10', '20', '30'},
                                        'autoNom-3600': {'0', '10', '20', '30'},
                                        'leftS-1080': {'0', '10', '20', '30'},
                                        'pass/dv': {'pass/dop/vid'}
                                    },
                                'pass': 'dop-fin'
                            },
                    },
                'stan10':
                    {
                        'saveDays':
                            {
                                '0':
                                    {
                                        'saveType':
                                            {
                                                'reg': 150
                                            }
                                    },
                                '3':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 178,
                                                        '1': 216,
                                                        '1.5': 243,
                                                        '2': 337
                                                    },
                                                'actions':
                                                    {
                                                        '512': 178,
                                                        '1': 189,
                                                        '1.5': 216,
                                                        '2': 305,
                                                        '3': 356
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 151
                                                    }

                                            }
                                    },
                                '5':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 194,
                                                        '1': 259,
                                                        '1.5': 376
                                                    },
                                                'actions':
                                                    {
                                                        '512': 194,
                                                        '1': 227,
                                                        '1.5': 337,
                                                        '3': 408
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 146
                                                    }

                                            }
                                    },
                                '7':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 259,
                                                        '1': 346,
                                                        '1.5': 389,
                                                        '2': 544
                                                    },
                                                'actions':
                                                    {
                                                        '512': 259,
                                                        '1': 302,
                                                        '1.5': 346,
                                                        '2': 480,
                                                        '3': 596
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 194
                                                    }

                                            }
                                    },
                                '10':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 389,
                                                        '1': 518,
                                                        '1.5': 583
                                                    },
                                                'actions':
                                                    {
                                                        '512': 389,
                                                        '1': 454,
                                                        '1.5': 518,
                                                        '3': 648
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 292
                                                    }

                                            }
                                    },
                                '14':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 486,
                                                        '1': 648,
                                                        '1.5': 729,
                                                        '2': 940
                                                    },
                                                'actions':
                                                    {
                                                        '512': 486,
                                                        '1': 567,
                                                        '1.5': 648,
                                                        '2': 894,
                                                        '3': 1017
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 365
                                                    }

                                            }
                                    },
                                '30':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 778,
                                                        '1': 1037,
                                                        '1.5': 1166,
                                                        '2': 1814
                                                    },
                                                'actions':
                                                    {
                                                        '512': 778,
                                                        '1': 907,
                                                        '1.5': 1037,
                                                        '2': 1555,
                                                        '3': 2916
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 583
                                                    }

                                            }
                                    },
                                '45':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 1166,
                                                        '1': 1555,
                                                        '1.5': 1750
                                                    },
                                                'actions':
                                                    {
                                                        '512': 1166,
                                                        '1': 1361,
                                                        '1.5': 1555,
                                                        '3': 2916
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 875
                                                    }

                                            }
                                    },
                                '60':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 1426,
                                                        '1': 1901,
                                                        '1.5': 2138
                                                    },
                                                'actions':
                                                    {
                                                        '512': 1426,
                                                        '1': 1663,
                                                        '1.5': 1901,
                                                        '3': 3823
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 1069
                                                    }

                                            }
                                    },
                                '90':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 2074,
                                                        '1': 2765,
                                                        '1.5': 3110
                                                    },
                                                'actions':
                                                    {
                                                        '512': 2074,
                                                        '1': 2419,
                                                        '1.5': 2765,
                                                        '3': 5573
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 1555
                                                    }

                                            }
                                    },
                                '180':
                                    {
                                        'saveType':
                                            {
                                                'actions':
                                                    {
                                                        '1.5': 6480
                                                    }

                                            }
                                    },

                            },
                        'dop':
                            {
                                'smsPack':
                                    {
                                        '100/30': 108,
                                        '500/90': 540,
                                        '1000/180': 1080,
                                        '5000/365': 5400
                                    },
                                'vidAnal': vn_vid_anal,
                                'pass': 'dop-fin'
                            }
                    },
                'stan20':
                    {
                        'saveDays':
                            {
                                '0':
                                    {
                                        'saveType':
                                            {
                                                'reg': 150
                                            }
                                    },
                                '3':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 158,
                                                        '1': 192,
                                                        '1.5': 216,
                                                        '2': 300
                                                    },
                                                'actions':
                                                    {
                                                        '512': 158,
                                                        '1': 168,
                                                        '1.5': 192,
                                                        '2': 271,
                                                        '3': 317
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 134
                                                    }

                                            }
                                    },
                                '5':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 173,
                                                        '1': 230,
                                                        '1.5': 334
                                                    },
                                                'actions':
                                                    {
                                                        '512': 173,
                                                        '1': 202,
                                                        '1.5': 300,
                                                        '3': 426
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 130
                                                    }

                                            }
                                    },
                                '7':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 230,
                                                        '1': 307,
                                                        '1.5': 346,
                                                        '2': 484
                                                    },
                                                'actions':
                                                    {
                                                        '512': 230,
                                                        '1': 269,
                                                        '1.5': 307,
                                                        '2': 426,
                                                        '3': 530
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 173
                                                    }

                                            }
                                    },
                                '10':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 346,
                                                        '1': 461,
                                                        '1.5': 518
                                                    },
                                                'actions':
                                                    {
                                                        '512': 230,
                                                        '1': 403,
                                                        '1.5': 461,
                                                        '3': 576
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 259
                                                    }

                                            }
                                    },
                                '14':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 432,
                                                        '1': 576,
                                                        '1.5': 648,
                                                        '2': 835
                                                    },
                                                'actions':
                                                    {
                                                        '512': 432,
                                                        '1': 504,
                                                        '1.5': 576,
                                                        '2': 795,
                                                        '3': 904
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 324
                                                    }

                                            }
                                    },
                                '30':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 691,
                                                        '1': 922,
                                                        '1.5': 1037,
                                                        '2': 1613
                                                    },
                                                'actions':
                                                    {
                                                        '512': 691,
                                                        '1': 806,
                                                        '1.5': 922,
                                                        '2': 1382,
                                                        '3': 1786
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 518
                                                    }

                                            }
                                    },
                                '45':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 1037,
                                                        '1': 1382,
                                                        '1.5': 1555
                                                    },
                                                'actions':
                                                    {
                                                        '512': 1037,
                                                        '1': 1210,
                                                        '1.5': 1382,
                                                        '3': 2592
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 778
                                                    }

                                            }
                                    },
                                '60':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 1267,
                                                        '1': 1690,
                                                        '1.5': 1901
                                                    },
                                                'actions':
                                                    {
                                                        '512': 1267,
                                                        '1': 1478,
                                                        '1.5': 1690,
                                                        '3': 3398
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 950
                                                    }

                                            }
                                    },
                                '90':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 1843,
                                                        '1': 2458,
                                                        '1.5': 2765
                                                    },
                                                'actions':
                                                    {
                                                        '512': 1843,
                                                        '1': 2150,
                                                        '1.5': 2458,
                                                        '3': 4954
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 1382
                                                    }

                                            }
                                    },
                                '180':
                                    {
                                        'saveType':
                                            {
                                                'actions':
                                                    {
                                                        '1.5': 5760
                                                    }

                                            }
                                    },

                            },
                        'dop':
                            {
                                'smsPack':
                                    {
                                        '100/30': 96,
                                        '500/90': 480,
                                        '1000/180': 960,
                                        '5000/365': 4800
                                    },
                                'vidAnal': vn_vid_anal,
                                'pass': 'dop-fin'
                            }

                    }
            },
        'vnBase':
            {
                'base20':
                    {
                        'saveDays':
                            {
                                '0':
                                    {
                                        'saveType':
                                            {
                                                'reg': 200
                                            }
                                    },
                                '3':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 300,
                                                        '1': 300,
                                                        '1.5': 300,
                                                        '2': 300
                                                    },
                                                'actions':
                                                    {
                                                        '512': 300,
                                                        '1': 300,
                                                        '1.5': 300,
                                                        '2': 300
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 300
                                                    }

                                            }
                                    },
                                '7':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 450,
                                                        '1': 450,
                                                        '1.5': 450,
                                                        '2': 450
                                                    },
                                                'actions':
                                                    {
                                                        '512': 450,
                                                        '1': 450,
                                                        '1.5': 450,
                                                        '2': 450
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 450
                                                    }

                                            }
                                    },
                                '14':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 600,
                                                        '1': 600,
                                                        '1.5': 600,
                                                        '2': 600
                                                    },
                                                'actions':
                                                    {
                                                        '512': 600,
                                                        '1': 600,
                                                        '1.5': 600,
                                                        '2': 600
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 600
                                                    }

                                            }
                                    },
                                '30':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 900,
                                                        '1': 900,
                                                        '1.5': 900,
                                                        '2': 900
                                                    },
                                                'actions':
                                                    {
                                                        '512': 900,
                                                        '1': 900,
                                                        '1.5': 900,
                                                        '2': 900
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 900
                                                    }

                                            }
                                    },
                                '45':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 1350,
                                                        '1': 1350,
                                                        '1.5': 1350,
                                                        '2': 1350
                                                    },
                                                'actions':
                                                    {
                                                        '512': 1350,
                                                        '1': 1350,
                                                        '1.5': 1350,
                                                        '2': 1350
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 1350
                                                    }

                                            }
                                    },
                                '60':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 1800,
                                                        '1': 1800,
                                                        '1.5': 1800,
                                                        '2': 1800
                                                    },
                                                'actions':
                                                    {
                                                        '512': 1800,
                                                        '1': 1800,
                                                        '1.5': 1800,
                                                        '2': 1800
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 1800
                                                    }

                                            }
                                    },
                                '90':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 2700,
                                                        '1': 2700,
                                                        '1.5': 2700,
                                                        '2': 2700
                                                    },
                                                'actions':
                                                    {
                                                        '512': 2700,
                                                        '1': 2700,
                                                        '1.5': 2700,
                                                        '2': 2700
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 2700
                                                    }

                                            }
                                    },
                                '180':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 5400,
                                                        '1': 5400,
                                                        '1.5': 5400,
                                                        '2': 5400
                                                    },
                                                'actions':
                                                    {
                                                        '512': 5400,
                                                        '1': 5400,
                                                        '1.5': 5400,
                                                        '2': 5400
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 5400
                                                    }

                                            }
                                    },

                            },
                        'dop':
                            {
                                'smsPack':
                                    {
                                        '100/30': 120,
                                        '500/90': 600,
                                        '1000/180': 1200,
                                        '5000/365': 6000
                                    },
                                'vidAnal': vn_vid_anal,
                                'pass': 'dop-fin'
                            }
                    },
                'base20mlm':
                    {
                        'saveDays':
                            {
                                '0':
                                    {
                                        'saveType':
                                            {
                                                'reg': 200
                                            }
                                    },
                                '3':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '256': 300
                                                    },
                                                'actions':
                                                    {
                                                        '256': 300
                                                    },

                                            }
                                    },
                                '7':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '256': 450
                                                    },
                                                'actions':
                                                    {
                                                        '256': 450
                                                    },

                                            }
                                    },
                                '14':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '256': 600
                                                    },
                                                'actions':
                                                    {
                                                        '256': 600
                                                    },

                                            }
                                    },
                                '30':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '256': 900
                                                    },
                                                'actions':
                                                    {
                                                        '256': 900
                                                    },

                                            }
                                    },
                                '45':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '256': 1350
                                                    },
                                                'actions':
                                                    {
                                                        '256': 1350
                                                    },

                                            }
                                    },
                                '60':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '256': 1800
                                                    },
                                                'actions':
                                                    {
                                                        '256': 1800
                                                    },

                                            }
                                    },
                                '90':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '256': 2700
                                                    },
                                                'actions':
                                                    {
                                                        '256': 2700
                                                    },

                                            }
                                    },
                                '180':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '256': 5400
                                                    },
                                                'actions':
                                                    {
                                                        '256': 5400
                                                    },

                                            }
                                    },

                            },
                        'dop':
                            {
                                'smsPack':
                                    {
                                        '100/30': 120,
                                        '500/90': 600,
                                        '1000/180': 1200,
                                        '5000/365': 6000
                                    },
                                'vidAnal': vn_vid_anal,
                                'pass': 'dop-fin'
                            },
                    },
                'base20dig':
                    {
                        'saveDays':
                            {
                                '0':
                                    {
                                        'saveType':
                                            {
                                                'reg': 200
                                            }
                                    },
                                '3':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 300,
                                                        '1': 300,
                                                        '1.5': 300,
                                                        '2': 300
                                                    },
                                                'actions':
                                                    {
                                                        '512': 300,
                                                        '1': 300,
                                                        '1.5': 300,
                                                        '2': 300
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 300
                                                    }

                                            }
                                    },
                                '7':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 450,
                                                        '1': 450,
                                                        '1.5': 450,
                                                        '2': 450
                                                    },
                                                'actions':
                                                    {
                                                        '512': 450,
                                                        '1': 450,
                                                        '1.5': 450,
                                                        '2': 450
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 450
                                                    }

                                            }
                                    },
                                '14':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 600,
                                                        '1': 600,
                                                        '1.5': 600,
                                                        '2': 600
                                                    },
                                                'actions':
                                                    {
                                                        '512': 600,
                                                        '1': 600,
                                                        '1.5': 600,
                                                        '2': 600
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 600
                                                    }

                                            }
                                    },
                                '30':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 900,
                                                        '1': 900,
                                                        '1.5': 900,
                                                        '2': 900
                                                    },
                                                'actions':
                                                    {
                                                        '512': 900,
                                                        '1': 900,
                                                        '1.5': 900,
                                                        '2': 900
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 900
                                                    }

                                            }
                                    },
                                '45':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 1350,
                                                        '1': 1350,
                                                        '1.5': 1350,
                                                        '2': 1350
                                                    },
                                                'actions':
                                                    {
                                                        '512': 1350,
                                                        '1': 1350,
                                                        '1.5': 1350,
                                                        '2': 1350
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 1350
                                                    }

                                            }
                                    },
                                '60':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 1800,
                                                        '1': 1800,
                                                        '1.5': 1800,
                                                        '2': 1800
                                                    },
                                                'actions':
                                                    {
                                                        '512': 1800,
                                                        '1': 1800,
                                                        '1.5': 1800,
                                                        '2': 1800
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 1800
                                                    }

                                            }
                                    },
                                '90':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 2700,
                                                        '1': 2700,
                                                        '1.5': 2700,
                                                        '2': 2700
                                                    },
                                                'actions':
                                                    {
                                                        '512': 2700,
                                                        '1': 2700,
                                                        '1.5': 2700,
                                                        '2': 2700
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 2700
                                                    }

                                            }
                                    },
                                '180':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 5400,
                                                        '1': 5400,
                                                        '1.5': 5400,
                                                        '2': 5400
                                                    },
                                                'actions':
                                                    {
                                                        '512': 5400,
                                                        '1': 5400,
                                                        '1.5': 5400,
                                                        '2': 5400
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 5400
                                                    }

                                            }
                                    },

                            },
                        'dop':
                            {
                                'smsPack':
                                    {
                                        '100/30': 120,
                                        '500/90': 600,
                                        '1000/180': 1200,
                                        '5000/365': 6000
                                    },
                                'vidAnal': vn_vid_anal,
                                'pass': 'dop-fin'
                            }
                    },
                'base2010':
                    {
                        'saveDays':
                            {
                                '0':
                                    {
                                        'saveType':
                                            {
                                                'reg': 180
                                            }
                                    },
                                '3':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 270,
                                                        '1': 270,
                                                        '1.5': 270,
                                                        '2': 270
                                                    },
                                                'actions':
                                                    {
                                                        '512': 270,
                                                        '1': 270,
                                                        '1.5': 270,
                                                        '2': 270
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 270
                                                    }

                                            }
                                    },
                                '7':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 405,
                                                        '1': 405,
                                                        '1.5': 405,
                                                        '2': 405
                                                    },
                                                'actions':
                                                    {
                                                        '512': 405,
                                                        '1': 405,
                                                        '1.5': 405,
                                                        '2': 405
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 405
                                                    }

                                            }
                                    },
                                '14':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 540,
                                                        '1': 540,
                                                        '1.5': 540,
                                                        '2': 540
                                                    },
                                                'actions':
                                                    {
                                                        '512': 540,
                                                        '1': 540,
                                                        '1.5': 540,
                                                        '2': 540
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 540
                                                    }

                                            }
                                    },
                                '30':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 810,
                                                        '1': 810,
                                                        '1.5': 810,
                                                        '2': 810
                                                    },
                                                'actions':
                                                    {
                                                        '512': 810,
                                                        '1': 810,
                                                        '1.5': 810,
                                                        '2': 810
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 810
                                                    }

                                            }
                                    },
                                '45':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 1215,
                                                        '1': 1215,
                                                        '1.5': 1215,
                                                        '2': 1215
                                                    },
                                                'actions':
                                                    {
                                                        '512': 1215,
                                                        '1': 1215,
                                                        '1.5': 1215,
                                                        '2': 1215
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 1215
                                                    }

                                            }
                                    },
                                '60':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 1620,
                                                        '1': 1620,
                                                        '1.5': 1620,
                                                        '2': 1620
                                                    },
                                                'actions':
                                                    {
                                                        '512': 1620,
                                                        '1': 1620,
                                                        '1.5': 1620,
                                                        '2': 1620
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 1620
                                                    }

                                            }
                                    },
                                '90':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 2430,
                                                        '1': 2430,
                                                        '1.5': 2430,
                                                        '2': 2430
                                                    },
                                                'actions':
                                                    {
                                                        '512': 2430,
                                                        '1': 2430,
                                                        '1.5': 2430,
                                                        '2': 2430
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 2430
                                                    }

                                            }
                                    },
                                '180':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 4860,
                                                        '1': 4860,
                                                        '1.5': 4860,
                                                        '2': 4860
                                                    },
                                                'actions':
                                                    {
                                                        '512': 4860,
                                                        '1': 4860,
                                                        '1.5': 4860,
                                                        '2': 4860
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 4860
                                                    }

                                            }
                                    },

                            },
                        'dop':
                            {
                                'smsPack':
                                    {
                                        '100/30': 120,
                                        '500/90': 600,
                                        '1000/180': 1200,
                                        '5000/365': 6000
                                    },
                                'vidAnal': vn_vid_anal,
                                'pass': 'dop-fin'
                            }
                    },
                'base2010mlm':
                    {
                        'saveDays':
                            {
                                '0':
                                    {
                                        'saveType':
                                            {
                                                'reg': 180
                                            }
                                    },
                                '3':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '256': 270
                                                    },
                                                'actions':
                                                    {
                                                        '256': 270
                                                    },

                                            }
                                    },
                                '7':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '256': 405
                                                    },
                                                'actions':
                                                    {
                                                        '256': 405
                                                    },

                                            }
                                    },
                                '14':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '256': 540
                                                    },
                                                'actions':
                                                    {
                                                        '256': 540
                                                    },

                                            }
                                    },
                                '30':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '256': 810
                                                    },
                                                'actions':
                                                    {
                                                        '256': 810
                                                    },

                                            }
                                    },
                                '45':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '256': 1215
                                                    },
                                                'actions':
                                                    {
                                                        '256': 1215
                                                    },

                                            }
                                    },
                                '60':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '256': 1620
                                                    },
                                                'actions':
                                                    {
                                                        '256': 1620
                                                    },

                                            }
                                    },
                                '90':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '256': 2430
                                                    },
                                                'actions':
                                                    {
                                                        '256': 2430
                                                    },

                                            }
                                    },
                                '180':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '256': 4860
                                                    },
                                                'actions':
                                                    {
                                                        '256': 4860
                                                    },

                                            }
                                    },

                            },
                        'dop':
                            {
                                'smsPack':
                                    {
                                        '100/30': 120,
                                        '500/90': 600,
                                        '1000/180': 1200,
                                        '5000/365': 6000
                                    },
                                'vidAnal': vn_vid_anal,
                                'pass': 'dop-fin'
                            }
                    },
                'base2010dig':
                    {
                        'saveDays':
                            {
                                '0':
                                    {
                                        'saveType':
                                            {
                                                'reg': 180
                                            }
                                    },
                                '3':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 270,
                                                        '1': 270,
                                                        '1.5': 270,
                                                        '2': 270
                                                    },
                                                'actions':
                                                    {
                                                        '512': 270,
                                                        '1': 270,
                                                        '1.5': 270,
                                                        '2': 270
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 270
                                                    }

                                            }
                                    },
                                '7':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 405,
                                                        '1': 405,
                                                        '1.5': 405,
                                                        '2': 405
                                                    },
                                                'actions':
                                                    {
                                                        '512': 405,
                                                        '1': 405,
                                                        '1.5': 405,
                                                        '2': 405
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 405
                                                    }

                                            }
                                    },
                                '14':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 540,
                                                        '1': 540,
                                                        '1.5': 540,
                                                        '2': 540
                                                    },
                                                'actions':
                                                    {
                                                        '512': 540,
                                                        '1': 540,
                                                        '1.5': 540,
                                                        '2': 540
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 540
                                                    }

                                            }
                                    },
                                '30':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 810,
                                                        '1': 810,
                                                        '1.5': 810,
                                                        '2': 810
                                                    },
                                                'actions':
                                                    {
                                                        '512': 810,
                                                        '1': 810,
                                                        '1.5': 810,
                                                        '2': 810
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 810
                                                    }

                                            }
                                    },
                                '45':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 1215,
                                                        '1': 1215,
                                                        '1.5': 1215,
                                                        '2': 1215
                                                    },
                                                'actions':
                                                    {
                                                        '512': 1215,
                                                        '1': 1215,
                                                        '1.5': 1215,
                                                        '2': 1215
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 1215
                                                    }

                                            }
                                    },
                                '60':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 1620,
                                                        '1': 1620,
                                                        '1.5': 1620,
                                                        '2': 1620
                                                    },
                                                'actions':
                                                    {
                                                        '512': 1620,
                                                        '1': 1620,
                                                        '1.5': 1620,
                                                        '2': 1620
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 1620
                                                    }

                                            }
                                    },
                                '90':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 2430,
                                                        '1': 2430,
                                                        '1.5': 2430,
                                                        '2': 2430
                                                    },
                                                'actions':
                                                    {
                                                        '512': 2430,
                                                        '1': 2430,
                                                        '1.5': 2430,
                                                        '2': 2430
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 2430
                                                    }

                                            }
                                    },
                                '180':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 4860,
                                                        '1': 4860,
                                                        '1.5': 4860,
                                                        '2': 4860
                                                    },
                                                'actions':
                                                    {
                                                        '512': 4860,
                                                        '1': 4860,
                                                        '1.5': 4860,
                                                        '2': 4860
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 4860
                                                    }

                                            }
                                    },

                            },
                        'dop':
                            {
                                'smsPack':
                                    {
                                        '100/30': 120,
                                        '500/90': 600,
                                        '1000/180': 1200,
                                        '5000/365': 6000
                                    },
                                'vidAnal': vn_vid_anal,
                                'pass': 'dop-fin'
                            }
                    },
                'base2020':
                    {
                        'saveDays':
                            {
                                '0':
                                    {
                                        'saveType':
                                            {
                                                'reg': 160
                                            }
                                    },
                                '3':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 240,
                                                        '1': 240,
                                                        '1.5': 240,
                                                        '2': 240
                                                    },
                                                'actions':
                                                    {
                                                        '512': 240,
                                                        '1': 240,
                                                        '1.5': 240,
                                                        '2': 240
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 240
                                                    }

                                            }
                                    },
                                '7':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 360,
                                                        '1': 360,
                                                        '1.5': 360,
                                                        '2': 360
                                                    },
                                                'actions':
                                                    {
                                                        '512': 360,
                                                        '1': 360,
                                                        '1.5': 360,
                                                        '2': 360
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 360
                                                    }

                                            }
                                    },
                                '14':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 480,
                                                        '1': 480,
                                                        '1.5': 480,
                                                        '2': 480
                                                    },
                                                'actions':
                                                    {
                                                        '512': 480,
                                                        '1': 480,
                                                        '1.5': 480,
                                                        '2': 480
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 480
                                                    }

                                            }
                                    },
                                '30':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 720,
                                                        '1': 720,
                                                        '1.5': 720,
                                                        '2': 720
                                                    },
                                                'actions':
                                                    {
                                                        '512': 720,
                                                        '1': 720,
                                                        '1.5': 720,
                                                        '2': 720
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 720
                                                    }

                                            }
                                    },
                                '45':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 1080,
                                                        '1': 1080,
                                                        '1.5': 1080,
                                                        '2': 1080
                                                    },
                                                'actions':
                                                    {
                                                        '512': 1080,
                                                        '1': 1080,
                                                        '1.5': 1080,
                                                        '2': 1080
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 1080
                                                    }

                                            }
                                    },
                                '60':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 1440,
                                                        '1': 1440,
                                                        '1.5': 1440,
                                                        '2': 1440
                                                    },
                                                'actions':
                                                    {
                                                        '512': 1440,
                                                        '1': 1440,
                                                        '1.5': 1440,
                                                        '2': 1440
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 1440
                                                    }

                                            }
                                    },
                                '90':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 2160,
                                                        '1': 2160,
                                                        '1.5': 2160,
                                                        '2': 2160
                                                    },
                                                'actions':
                                                    {
                                                        '512': 2160,
                                                        '1': 2160,
                                                        '1.5': 2160,
                                                        '2': 2160
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 2160
                                                    }

                                            }
                                    },
                                '180':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 4320,
                                                        '1': 4320,
                                                        '1.5': 4320,
                                                        '2': 4320
                                                    },
                                                'actions':
                                                    {
                                                        '512': 4320,
                                                        '1': 4320,
                                                        '1.5': 4320,
                                                        '2': 4320
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 4320
                                                    }

                                            }
                                    },

                            },
                        'dop':
                            {
                                'smsPack':
                                    {
                                        '100/30': 120,
                                        '500/90': 600,
                                        '1000/180': 1200,
                                        '5000/365': 6000
                                    },
                                'vidAnal': vn_vid_anal,
                                'pass': 'dop-fin'
                            }
                    },
                'base2020mlm':
                    {
                        'saveDays':
                            {
                                '0':
                                    {
                                        'saveType':
                                            {
                                                'reg': 160
                                            }
                                    },
                                '3':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '256': 240
                                                    },
                                                'actions':
                                                    {
                                                        '256': 240
                                                    },

                                            }
                                    },
                                '7':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '256': 360
                                                    },
                                                'actions':
                                                    {
                                                        '256': 360
                                                    },

                                            }
                                    },
                                '14':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '256': 480
                                                    },
                                                'actions':
                                                    {
                                                        '256': 480
                                                    },

                                            }
                                    },
                                '30':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '256': 720
                                                    },
                                                'actions':
                                                    {
                                                        '256': 720
                                                    },

                                            }
                                    },
                                '45':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '256': 1080
                                                    },
                                                'actions':
                                                    {
                                                        '256': 1080
                                                    },

                                            }
                                    },
                                '60':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '256': 1440
                                                    },
                                                'actions':
                                                    {
                                                        '256': 1440
                                                    },

                                            }
                                    },
                                '90':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '256': 2160
                                                    },
                                                'actions':
                                                    {
                                                        '256': 2160
                                                    },

                                            }
                                    },
                                '180':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '256': 4320
                                                    },
                                                'actions':
                                                    {
                                                        '256': 4320
                                                    },

                                            }
                                    },

                            },
                        'dop':
                            {
                                'smsPack':
                                    {
                                        '100/30': 120,
                                        '500/90': 600,
                                        '1000/180': 1200,
                                        '5000/365': 6000
                                    },
                                'vidAnal': vn_vid_anal,
                                'pass': 'dop-fin'
                            }
                    },
                'base2020dig':
                    {
                        'saveDays':
                            {
                                '0':
                                    {
                                        'saveType':
                                            {
                                                'reg': 160
                                            }
                                    },
                                '3':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 240,
                                                        '1': 240,
                                                        '1.5': 240,
                                                        '2': 240
                                                    },
                                                'actions':
                                                    {
                                                        '512': 240,
                                                        '1': 240,
                                                        '1.5': 240,
                                                        '2': 240
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 240
                                                    }

                                            }
                                    },
                                '7':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 360,
                                                        '1': 360,
                                                        '1.5': 360,
                                                        '2': 360
                                                    },
                                                'actions':
                                                    {
                                                        '512': 360,
                                                        '1': 360,
                                                        '1.5': 360,
                                                        '2': 360
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 360
                                                    }

                                            }
                                    },
                                '14':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 480,
                                                        '1': 480,
                                                        '1.5': 480,
                                                        '2': 480
                                                    },
                                                'actions':
                                                    {
                                                        '512': 480,
                                                        '1': 480,
                                                        '1.5': 480,
                                                        '2': 480
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 480
                                                    }

                                            }
                                    },
                                '30':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 720,
                                                        '1': 720,
                                                        '1.5': 720,
                                                        '2': 720
                                                    },
                                                'actions':
                                                    {
                                                        '512': 720,
                                                        '1': 720,
                                                        '1.5': 720,
                                                        '2': 720
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 720
                                                    }

                                            }
                                    },
                                '45':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 1080,
                                                        '1': 1080,
                                                        '1.5': 1080,
                                                        '2': 1080
                                                    },
                                                'actions':
                                                    {
                                                        '512': 1080,
                                                        '1': 1080,
                                                        '1.5': 1080,
                                                        '2': 1080
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 1080
                                                    }

                                            }
                                    },
                                '60':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 1440,
                                                        '1': 1440,
                                                        '1.5': 1440,
                                                        '2': 1440
                                                    },
                                                'actions':
                                                    {
                                                        '512': 1440,
                                                        '1': 1440,
                                                        '1.5': 1440,
                                                        '2': 1440
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 1440
                                                    }

                                            }
                                    },
                                '90':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 2160,
                                                        '1': 2160,
                                                        '1.5': 2160,
                                                        '2': 2160
                                                    },
                                                'actions':
                                                    {
                                                        '512': 2160,
                                                        '1': 2160,
                                                        '1.5': 2160,
                                                        '2': 2160
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 2160
                                                    }

                                            }
                                    },
                                '180':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 4320,
                                                        '1': 4320,
                                                        '1.5': 4320,
                                                        '2': 4320
                                                    },
                                                'actions':
                                                    {
                                                        '512': 4320,
                                                        '1': 4320,
                                                        '1.5': 4320,
                                                        '2': 4320
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 4320
                                                    }

                                            }
                                    },

                            },
                        'dop':
                            {
                                'smsPack':
                                    {
                                        '100/30': 120,
                                        '500/90': 600,
                                        '1000/180': 1200,
                                        '5000/365': 6000
                                    },
                                'vidAnal': vn_vid_anal,
                                'pass': 'dop-fin'
                            }
                    },
                'base2030':
                    {
                        'saveDays':
                            {
                                '0':
                                    {
                                        'saveType':
                                            {
                                                'reg': 140
                                            }
                                    },
                                '3':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 210,
                                                        '1': 210,
                                                        '1.5': 210,
                                                        '2': 210
                                                    },
                                                'actions':
                                                    {
                                                        '512': 210,
                                                        '1': 210,
                                                        '1.5': 210,
                                                        '2': 210
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 210
                                                    }

                                            }
                                    },
                                '7':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 315,
                                                        '1': 315,
                                                        '1.5': 315,
                                                        '2': 315
                                                    },
                                                'actions':
                                                    {
                                                        '512': 315,
                                                        '1': 315,
                                                        '1.5': 315,
                                                        '2': 315
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 315
                                                    }

                                            }
                                    },
                                '14':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 420,
                                                        '1': 420,
                                                        '1.5': 420,
                                                        '2': 420
                                                    },
                                                'actions':
                                                    {
                                                        '512': 420,
                                                        '1': 420,
                                                        '1.5': 420,
                                                        '2': 420
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 420
                                                    }

                                            }
                                    },
                                '30':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 630,
                                                        '1': 630,
                                                        '1.5': 630,
                                                        '2': 630
                                                    },
                                                'actions':
                                                    {
                                                        '512': 630,
                                                        '1': 630,
                                                        '1.5': 630,
                                                        '2': 630
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 630
                                                    }

                                            }
                                    },
                                '45':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 945,
                                                        '1': 945,
                                                        '1.5': 945,
                                                        '2': 945
                                                    },
                                                'actions':
                                                    {
                                                        '512': 945,
                                                        '1': 945,
                                                        '1.5': 945,
                                                        '2': 945
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 945
                                                    }

                                            }
                                    },
                                '60':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 1260,
                                                        '1': 1260,
                                                        '1.5': 1260,
                                                        '2': 1260
                                                    },
                                                'actions':
                                                    {
                                                        '512': 1260,
                                                        '1': 1260,
                                                        '1.5': 1260,
                                                        '2': 1260
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 1260
                                                    }

                                            }
                                    },
                                '90':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 1890,
                                                        '1': 1890,
                                                        '1.5': 1890,
                                                        '2': 1890
                                                    },
                                                'actions':
                                                    {
                                                        '512': 1890,
                                                        '1': 1890,
                                                        '1.5': 1890,
                                                        '2': 1890
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 1890
                                                    }

                                            }
                                    },
                                '180':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 3780,
                                                        '1': 3780,
                                                        '1.5': 3780,
                                                        '2': 3780
                                                    },
                                                'actions':
                                                    {
                                                        '512': 3780,
                                                        '1': 3780,
                                                        '1.5': 3780,
                                                        '2': 3780
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 3780
                                                    }

                                            }
                                    },

                            },
                        'dop':
                            {
                                'smsPack':
                                    {
                                        '100/30': 120,
                                        '500/90': 600,
                                        '1000/180': 1200,
                                        '5000/365': 6000
                                    },
                                'vidAnal': vn_vid_anal,
                                'pass': 'dop-fin'
                            }
                    },
                'base2030mlm':
                    {
                        'saveDays':
                            {
                                '0':
                                    {
                                        'saveType':
                                            {
                                                'reg': 140
                                            }
                                    },
                                '3':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '256': 210
                                                    },
                                                'actions':
                                                    {
                                                        '256': 210
                                                    },

                                            }
                                    },
                                '7':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '256': 315
                                                    },
                                                'actions':
                                                    {
                                                        '256': 315
                                                    },

                                            }
                                    },
                                '14':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '256': 420
                                                    },
                                                'actions':
                                                    {
                                                        '256': 420
                                                    },

                                            }
                                    },
                                '30':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '256': 630
                                                    },
                                                'actions':
                                                    {
                                                        '256': 630
                                                    },

                                            }
                                    },
                                '45':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '256': 945
                                                    },
                                                'actions':
                                                    {
                                                        '256': 945
                                                    },

                                            }
                                    },
                                '60':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '256': 1440
                                                    },
                                                'actions':
                                                    {
                                                        '256': 1440
                                                    },

                                            }
                                    },
                                '90':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '256': 1260
                                                    },
                                                'actions':
                                                    {
                                                        '256': 1260
                                                    },

                                            }
                                    },
                                '180':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '256': 1890
                                                    },
                                                'actions':
                                                    {
                                                        '256': 1890
                                                    },

                                            }
                                    },

                            },
                        'dop':
                            {
                                'smsPack':
                                    {
                                        '100/30': 120,
                                        '500/90': 600,
                                        '1000/180': 1200,
                                        '5000/365': 6000
                                    },
                                'vidAnal': vn_vid_anal,
                                'pass': 'dop-fin'
                            }
                    },
                'base2030dig':
                    {
                        'saveDays':
                            {
                                '0':
                                    {
                                        'saveType':
                                            {
                                                'reg': 140
                                            }
                                    },
                                '3':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 210,
                                                        '1': 210,
                                                        '1.5': 210,
                                                        '2': 210
                                                    },
                                                'actions':
                                                    {
                                                        '512': 210,
                                                        '1': 210,
                                                        '1.5': 210,
                                                        '2': 210
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 210
                                                    }

                                            }
                                    },
                                '7':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 315,
                                                        '1': 315,
                                                        '1.5': 315,
                                                        '2': 315
                                                    },
                                                'actions':
                                                    {
                                                        '512': 315,
                                                        '1': 315,
                                                        '1.5': 315,
                                                        '2': 315
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 315
                                                    }

                                            }
                                    },
                                '14':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 420,
                                                        '1': 420,
                                                        '1.5': 420,
                                                        '2': 420
                                                    },
                                                'actions':
                                                    {
                                                        '512': 420,
                                                        '1': 420,
                                                        '1.5': 420,
                                                        '2': 420
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 420
                                                    }

                                            }
                                    },
                                '30':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 630,
                                                        '1': 630,
                                                        '1.5': 630,
                                                        '2': 630
                                                    },
                                                'actions':
                                                    {
                                                        '512': 630,
                                                        '1': 630,
                                                        '1.5': 630,
                                                        '2': 630
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 630
                                                    }

                                            }
                                    },
                                '45':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 945,
                                                        '1': 945,
                                                        '1.5': 945,
                                                        '2': 945
                                                    },
                                                'actions':
                                                    {
                                                        '512': 945,
                                                        '1': 945,
                                                        '1.5': 945,
                                                        '2': 945
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 945
                                                    }

                                            }
                                    },
                                '60':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 1260,
                                                        '1': 1260,
                                                        '1.5': 1260,
                                                        '2': 1260
                                                    },
                                                'actions':
                                                    {
                                                        '512': 1260,
                                                        '1': 1260,
                                                        '1.5': 1260,
                                                        '2': 1260
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 1260
                                                    }

                                            }
                                    },
                                '90':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 1890,
                                                        '1': 1890,
                                                        '1.5': 1890,
                                                        '2': 1890
                                                    },
                                                'actions':
                                                    {
                                                        '512': 1890,
                                                        '1': 1890,
                                                        '1.5': 1890,
                                                        '2': 1890
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 1890
                                                    }

                                            }
                                    },
                                '180':
                                    {
                                        'saveType':
                                            {
                                                'complete':
                                                    {
                                                        '512': 3780,
                                                        '1': 3780,
                                                        '1.5': 3780,
                                                        '2': 3780
                                                    },
                                                'actions':
                                                    {
                                                        '512': 3780,
                                                        '1': 3780,
                                                        '1.5': 3780,
                                                        '2': 3780
                                                    },
                                                'econom':
                                                    {
                                                        'econom': 3780
                                                    }

                                            }
                                    },

                            },
                        'dop':
                            {
                                'smsPack':
                                    {
                                        '100/30': 120,
                                        '500/90': 600,
                                        '1000/180': 1200,
                                        '5000/365': 6000
                                    },
                                'vidAnal': vn_vid_anal,
                                'pass': 'dop-fin'
                            }
                    },
            }
    }

iptv_hot_dopch = \
    {
        'ihkhlprime': 149,
        'ihmatch': 100,
        'ihsupermatch': 450,
        'ihadult': 500,
        'ihadult+': 1200,
        'ihadultSut': 120,
        'ihadult+Sut': 360,
        'ihchina': 150,
        'ihchinaSut': 13,
        'ihpass/dopchannel': 'dopchannel-fin'
    }

iptv_hot_tariff = \
    {
        '1mainChNoInt':
            {
                'main':
                    {
                        '1st':
                            {'1/10': 240, '11/20': 220, '21/30': 200, '30+': 170},
                        '1lux':
                            {'1/10': 360, '11/20': 330, '21/30': 290, '30+': 260},
                        '1prestige':
                            {'1/10': 720, '11/20': 650, '21/30': 580, '30+': 510},
                        '1st/daily': 20,
                        '1lux/daily': 25,
                        '1prestige/daily': 50
                    },
                'dopchannel': iptv_hot_dopch,
                'infochannel':
                    {
                        '1': 0, '2': 60, '3': 75, '4': 95, '5': 120,
                        'pass/infochannel': 'infochannel-fin'
                    }
            },
        '2mainChPMS':
            {
                'main':
                    {
                        '2st/int': 300,
                        '2lux/int': 420,
                        '2prestige/int': 780,
                        '2st/daily/int': 25,
                        '2lux/daily/int': 30,
                        '2prestige/daily/int': 55
                    },
                'dopchannel': iptv_hot_dopch,
                'infochannel':
                    {
                        '1': 0, '2': 60, '3': 75, '4': 95, '5': 120,
                        'pass/infochannel': 'infochannel-fin'
                    }

            },
        '3mainChDVB':
            {
                'main':
                    {
                        '3st/dvb':
                            {'1/10': 240, '11/20': 220, '21/30': 200, '30+': 170},
                        '3lux/dvb':
                            {'1/10': 360, '11/20': 330, '21/30': 290, '30+': 260},
                        '3prestige/dvb':
                            {'1/10': 720, '11/20': 650, '21/30': 580, '30+': 510},
                        '3st/light/dvb':
                            {'1/10': 240, '11/20': 220, '21/30': 200, '30+': 170}
                    },
                'dopchannel': iptv_hot_dopch,
                'infochannel':
                    {
                        '1': 0, '2': 60, '3': 75, '4': 95, '5': 120,
                        'pass/infochannel': 'infochannel-fin'
                    }
            },
        '4mainChSmart':
            {
                'main':
                    {
                        '4st/smart':
                            {'1/10': 240, '11/20': 220, '21/30': 200, '30+': 170},
                        '4lux/smart':
                            {'1/10': 360, '11/20': 330, '21/30': 290, '30+': 260},
                        '4prestige/smart':
                            {'1/10': 720, '11/20': 650, '21/30': 580, '30+': 510},
                        '4st/daily/smart': 20,
                        '4lux/daily/smart': 25,
                        '4prestige/daily/smart': 50
                    },
                'dopchannel': iptv_hot_dopch,
                'infochannel':
                    {
                        '1': 0, '2': 60, '3': 75, '4': 95, '5': 120,
                        'pass/infochannel': 'infochannel-fin'
                    }
            },
        '5mainChSmartPMS':
            {
                'main':
                    {
                        '5st/smart/int': 300,
                        '5lux/smart/int': 420,
                        '5prestige/smart/int': 780,
                        '5st/daily/smart/int': 25,
                        '5lux/daily/smart/int': 30,
                        '5prestige/daily/smart/int': 55,
                        '5partner': 240,
                        '5partner/int': 300
                    },
                'dopchannel': iptv_hot_dopch,
                'infochannel':
                    {
                        '1': 0, '2': 60, '3': 75, '4': 95, '5': 120,
                        'pass/infochannel': 'infochannel-fin'
                    }
            }
    }

internet_tariff = \
    {
    'amur':
        {
            'opt':
             {
                 'yesm2m':
                  {
                      'm2mkontrol': [{'speed': '128k', 'discount': '30%', 'price': 180},
                                                                {'speed': '256k', 'discount': '30%', 'price': 240},
                                                                {'speed': '512k', 'discount': '30%', 'price': 300},
                                                                {'speed': '1M', 'discount': '30%', 'price': 480},
                                                                {'speed': '2M', 'discount': '30%', 'price': 720},
                                                                {'speed': '4M', 'discount': '30%', 'price': 960},
                                                                {'speed': '5M', 'discount': '30%', 'price': 1200}]
                  },
                  'nom2m':
                      {
                          'skorost': [{'speed': '30M', 'discount': '30%', 'price': 2800},
                                                            {'speed': '40M', 'discount': '30%', 'price': 3900},
                                                            {'speed': '50M', 'discount': '30%', 'price': 5500},
                                                            {'speed': '70M', 'discount': '30%', 'price': 7700},
                                                            {'speed': '100M', 'discount': '30%', 'price': 10800},
                                                            {'speed': '120M', 'discount': '30%', 'price': 15100},
                                                            {'speed': '150M', 'discount': '30%', 'price': 21100},
                                                            {'speed': '200M', 'discount': '30%', 'price': 29500},
                                                            {'speed': '250M', 'discount': '30%', 'price': 41300},
                                                            {'speed': '300M', 'discount': '30%', 'price': 57800}],
                          'ozhn': [{'speed': '30M', 'discount': 0, 'price': 1300},
                                                         {'speed': '50M', 'discount': 0, 'price': 2500},
                                                         {'speed': '100M', 'discount': 0, 'price': 5000}],
                          'uskorenie': [{'speed': '50M', 'discount': 0, 'price': 3400},
                                                              {'speed': '100M', 'discount': 0, 'price': 6500},
                                                              {'speed': '150M', 'discount': 0, 'price': 12500}]
                      }
             },
            'med':
                {
                    'yesm2m': {'m2mkontrol': [{'speed': '128k', 'discount': '30%', 'price': 180},
                                                                {'speed': '256k', 'discount': '30%', 'price': 240},
                                                                {'speed': '512k', 'discount': '30%', 'price': 300},
                                                                {'speed': '1M', 'discount': '30%', 'price': 480},
                                                                {'speed': '2M', 'discount': '30%', 'price': 720},
                                                                {'speed': '4M', 'discount': '30%', 'price': 960},
                                                                {'speed': '5M', 'discount': '30%', 'price': 1200}]},
                    'nom2m': {'delovoj': [{'speed': '4M', 'discount': '30%', 'price': 1500},
                                                            {'speed': '6M', 'discount': '30%', 'price': 2000},
                                                            {'speed': '8M', 'discount': '30%', 'price': 3000},
                                                            {'speed': '10M', 'discount': '30%', 'price': 4000}]}
                }
        },
    'kamch':
        {
            'opt': {'yesm2m': {'m2mkontrol': [{'speed': '128k', 'discount': '30%', 'price': 300},
                                                                 {'speed': '256k', 'discount': '30%', 'price': 360},
                                                                 {'speed': '512k', 'discount': '30%', 'price': 480},
                                                                 {'speed': '1M', 'discount': '30%', 'price': 780},
                                                                 {'speed': '2M', 'discount': '30%', 'price': 1080},
                                                                 {'speed': '4M', 'discount': '30%', 'price': 1440},
                                                                 {'speed': '5M', 'discount': '30%', 'price': 1800}]},
                                       'nom2m': {'skorost': [{'speed': '30M', 'discount': '30%', 'price': 3500},
                                                             {'speed': '40M', 'discount': '30%', 'price': 6000},
                                                             {'speed': '50M', 'discount': '30%', 'price': 8400},
                                                             {'speed': '70M', 'discount': '30%', 'price': 11800},
                                                             {'speed': '100M', 'discount': '30%', 'price': 16500},
                                                             {'speed': '120M', 'discount': '30%', 'price': 22400},
                                                             {'speed': '150M', 'discount': '30%', 'price': 32300},
                                                             {'speed': '200M', 'discount': '30%', 'price': 45200},
                                                             {'speed': '250M', 'discount': '30%', 'price': 63300},
                                                             {'speed': '300M', 'discount': '30%', 'price': 88800}],
                                                 'ozhn': [{'speed': '50M', 'discount': 0, 'price': 4000},
                                                          {'speed': '100M', 'discount': 0, 'price': 8000}],
                                                 'uskorenie': [{'speed': '50M', 'discount': 0, 'price': 4700},
                                                               {'speed': '100M', 'discount': 0, 'price': 10000},
                                                               {'speed': '150M', 'discount': 0, 'price': 19000}]}},
                               'med': {'yesm2m': {'m2mkontrol': [{'speed': '128k', 'discount': '30%', 'price': 360},
                                                                 {'speed': '256k', 'discount': '30%', 'price': 480},
                                                                 {'speed': '512k', 'discount': '30%', 'price': 600},
                                                                 {'speed': '1M', 'discount': '30%', 'price': 840},
                                                                 {'speed': '2M', 'discount': '30%', 'price': 1080},
                                                                 {'speed': '4M', 'discount': '30%', 'price': 1440},
                                                                 {'speed': '5M', 'discount': '30%', 'price': 1800}]},
                                       'nom2m': {'delovoj': [{'speed': '4M', 'discount': '30%', 'price': 2000},
                                                             {'speed': '6M', 'discount': '30%', 'price': 3000},
                                                             {'speed': '8M', 'discount': '30%', 'price': 4000},
                                                             {'speed': '10M', 'discount': '30%', 'price': 5000}]}}},
    'maga':
        {
            'opt': {'yesm2m': {'m2mkontrol': [{'speed': '128k', 'discount': '30%', 'price': 360},
                                                                {'speed': '256k', 'discount': '30%', 'price': 480},
                                                                {'speed': '512k', 'discount': '30%', 'price': 600},
                                                                {'speed': '1M', 'discount': '30%', 'price': 840},
                                                                {'speed': '2M', 'discount': '30%', 'price': 1080},
                                                                {'speed': '4M', 'discount': '30%', 'price': 1440},
                                                                {'speed': '5M', 'discount': '30%', 'price': 1800}]},
                                      'nom2m': {'skorost': [{'speed': '30M', 'discount': '30%', 'price': 6900},
                                                            {'speed': '40M', 'discount': '30%', 'price': 9300},
                                                            {'speed': '50M', 'discount': '30%', 'price': 12500},
                                                            {'speed': '70M', 'discount': '30%', 'price': 16300},
                                                            {'speed': '100M', 'discount': '30%', 'price': 21500},
                                                            {'speed': '120M', 'discount': '30%', 'price': 27500},
                                                            {'speed': '150M', 'discount': '30%', 'price': 36900},
                                                            {'speed': '200M', 'discount': '30%', 'price': 46300},
                                                            {'speed': '250M', 'discount': '30%', 'price': 61800},
                                                            {'speed': '300M', 'discount': '30%', 'price': 81500}],
                                                'ozhn': [{'speed': '30M', 'discount': 0, 'price': 2500},
                                                         {'speed': '50M', 'discount': 0, 'price': 4000},
                                                         {'speed': '100M', 'discount': 0, 'price': 9000}],
                                                'uskorenie': [{'speed': '50M', 'discount': 0, 'price': 8000},
                                                              {'speed': '100M', 'discount': 0, 'price': 13500},
                                                              {'speed': '150M', 'discount': 0, 'price': 23500}]}},
                              'med': {'yesm2m': {'m2mkontrol': [{'speed': '128k', 'discount': '30%', 'price': 360},
                                                                {'speed': '256k', 'discount': '30%', 'price': 480},
                                                                {'speed': '512k', 'discount': '30%', 'price': 600},
                                                                {'speed': '1M', 'discount': '30%', 'price': 840},
                                                                {'speed': '2M', 'discount': '30%', 'price': 1080},
                                                                {'speed': '4M', 'discount': '30%', 'price': 1440},
                                                                {'speed': '5M', 'discount': '30%', 'price': 1800}]},
                                      'nom2m': {'delovoj': [{'speed': '4M', 'discount': '30%', 'price': 2500},
                                                            {'speed': '6M', 'discount': '30%', 'price': 3000},
                                                            {'speed': '8M', 'discount': '30%', 'price': 4000},
                                                            {'speed': '10M', 'discount': '30%', 'price': 5000}]}}},
    'prim':
        {
            'opt': {'yesm2m': {'m2mkontrol': [{'speed': '128k', 'discount': '30%', 'price': 180},
                                                                {'speed': '256k', 'discount': '30%', 'price': 240},
                                                                {'speed': '512k', 'discount': '30%', 'price': 300},
                                                                {'speed': '1M', 'discount': '30%', 'price': 480},
                                                                {'speed': '2M', 'discount': '30%', 'price': 720},
                                                                {'speed': '4M', 'discount': '30%', 'price': 960},
                                                                {'speed': '5M', 'discount': '30%', 'price': 1200}]},
                                      'nom2m': {'skorost': [{'speed': '30M', 'discount': '30%', 'price': 3000},
                                                            {'speed': '40M', 'discount': '30%', 'price': 4200},
                                                            {'speed': '50M', 'discount': '30%', 'price': 5900},
                                                            {'speed': '70M', 'discount': '30%', 'price': 8300},
                                                            {'speed': '100M', 'discount': '30%', 'price': 11700},
                                                            {'speed': '120M', 'discount': '30%', 'price': 16300},
                                                            {'speed': '150M', 'discount': '30%', 'price': 22800},
                                                            {'speed': '200M', 'discount': '30%', 'price': 31900},
                                                            {'speed': '250M', 'discount': '30%', 'price': 41200},
                                                            {'speed': '300M', 'discount': '30%', 'price': 57600}],
                                                'ozhn': [{'speed': '30M', 'discount': 0, 'price': 1300},
                                                         {'speed': '50M', 'discount': 0, 'price': 2500},
                                                         {'speed': '100M', 'discount': 0, 'price': 5000}],
                                                'uskorenie': [{'speed': '50M', 'discount': 0, 'price': 3500},
                                                              {'speed': '100M', 'discount': 0, 'price': 7000},
                                                              {'speed': '150M', 'discount': 0, 'price': 13000}]}},
                              'med': {'yesm2m': {'m2mkontrol': [{'speed': '128k', 'discount': '30%', 'price': 180},
                                                                {'speed': '256k', 'discount': '30%', 'price': 240},
                                                                {'speed': '512k', 'discount': '30%', 'price': 300},
                                                                {'speed': '1M', 'discount': '30%', 'price': 480},
                                                                {'speed': '2M', 'discount': '30%', 'price': 720},
                                                                {'speed': '4M', 'discount': '30%', 'price': 960},
                                                                {'speed': '5M', 'discount': '30%', 'price': 1200}]},
                                      'nom2m': {'delovoj': [{'speed': '4M', 'discount': '30%', 'price': 1500},
                                                            {'speed': '6M', 'discount': '30%', 'price': 2000},
                                                            {'speed': '8M', 'discount': '30%', 'price': 3000},
                                                            {'speed': '10M', 'discount': '30%', 'price': 4000}]}}},
    'sakh':
        {
            'opt': {'yesm2m': {'m2mkontrol': [{'speed': '128k', 'discount': '30%', 'price': 300},
                                                                {'speed': '256k', 'discount': '30%', 'price': 360},
                                                                {'speed': '512k', 'discount': '30%', 'price': 420},
                                                                {'speed': '1M', 'discount': '30%', 'price': 720},
                                                                {'speed': '2M', 'discount': '30%', 'price': 960},
                                                                {'speed': '4M', 'discount': '30%', 'price': 1200},
                                                                {'speed': '5M', 'discount': '30%', 'price': 1440}]},
                                      'nom2m': {'skorost': [{'speed': '30M', 'discount': '30%', 'price': 3500},
                                                            {'speed': '40M', 'discount': '30%', 'price': 5000},
                                                            {'speed': '50M', 'discount': '30%', 'price': 7000},
                                                            {'speed': '70M', 'discount': '30%', 'price': 9700},
                                                            {'speed': '100M', 'discount': '30%', 'price': 13600},
                                                            {'speed': '120M', 'discount': '30%', 'price': 17700},
                                                            {'speed': '150M', 'discount': '30%', 'price': 23200},
                                                            {'speed': '200M', 'discount': '30%', 'price': 30100},
                                                            {'speed': '250M', 'discount': '30%', 'price': 39100},
                                                            {'speed': '300M', 'discount': '30%', 'price': 50800}],
                                                'ozhn': [{'speed': '30M', 'discount': 0, 'price': 1500},
                                                         {'speed': '50M', 'discount': 0, 'price': 3700},
                                                         {'speed': '100M', 'discount': 0, 'price': 7300}],
                                                'uskorenie': [{'speed': '50M', 'discount': 0, 'price': 4200},
                                                              {'speed': '100M', 'discount': 0, 'price': 8000},
                                                              {'speed': '150M', 'discount': 0, 'price': 15000}]}},
                              'med': {'yesm2m': {'m2mkontrol': [{'speed': '128k', 'discount': '30%', 'price': 300},
                                                                {'speed': '256k', 'discount': '30%', 'price': 360},
                                                                {'speed': '512k', 'discount': '30%', 'price': 420},
                                                                {'speed': '1M', 'discount': '30%', 'price': 720},
                                                                {'speed': '2M', 'discount': '30%', 'price': 960},
                                                                {'speed': '4M', 'discount': '30%', 'price': 1200},
                                                                {'speed': '5M', 'discount': '30%', 'price': 1440}]},
                                      'nom2m': {'delovoj': [{'speed': '4M', 'discount': '30%', 'price': 1500},
                                                            {'speed': '6M', 'discount': '30%', 'price': 2000},
                                                            {'speed': '8M', 'discount': '30%', 'price': 3000},
                                                            {'speed': '10M', 'discount': '30%', 'price': 4000}]}}},
    'sakhtel':
        {
            'opt': {'yesm2m': {'m2mkontrol': [{'speed': '128k', 'discount': '30%', 'price': 300},
                                                                   {'speed': '256k', 'discount': '30%', 'price': 360},
                                                                   {'speed': '512k', 'discount': '30%', 'price': 420},
                                                                   {'speed': '1M', 'discount': '30%', 'price': 720},
                                                                   {'speed': '2M', 'discount': '30%', 'price': 960},
                                                                   {'speed': '4M', 'discount': '30%', 'price': 1200},
                                                                   {'speed': '5M', 'discount': '30%', 'price': 1440}]},
                                         'nom2m': {'skorost': [{'speed': '30M', 'discount': '30%', 'price': 6000},
                                                               {'speed': '40M', 'discount': '30%', 'price': 8400},
                                                               {'speed': '50M', 'discount': '30%', 'price': 11800},
                                                               {'speed': '70M', 'discount': '30%', 'price': 16500},
                                                               {'speed': '100M', 'discount': '30%', 'price': 21500},
                                                               {'speed': '120M', 'discount': '30%', 'price': 28000},
                                                               {'speed': '150M', 'discount': '30%', 'price': 37000},
                                                               {'speed': '200M', 'discount': '30%', 'price': 48000},
                                                               {'speed': '250M', 'discount': '30%', 'price': 62400},
                                                               {'speed': '300M', 'discount': '30%', 'price': 81100}],
                                                   'ozhn': [{'speed': '30M', 'discount': 0, 'price': 2000},
                                                            {'speed': '50M', 'discount': 0, 'price': 4000},
                                                            {'speed': '100M', 'discount': 0, 'price': 8000}],
                                                   'uskorenie': [{'speed': '50M', 'discount': 0, 'price': 7000},
                                                                 {'speed': '100M', 'discount': 0, 'price': 13500},
                                                                 {'speed': '150M', 'discount': 0, 'price': 24000}]}},
                                 'med': {'yesm2m': {'m2mkontrol': [{'speed': '128k', 'discount': '30%', 'price': 300},
                                                                   {'speed': '256k', 'discount': '30%', 'price': 360},
                                                                   {'speed': '512k', 'discount': '30%', 'price': 420},
                                                                   {'speed': '1M', 'discount': '30%', 'price': 720},
                                                                   {'speed': '2M', 'discount': '30%', 'price': 960},
                                                                   {'speed': '4M', 'discount': '30%', 'price': 1200},
                                                                   {'speed': '5M', 'discount': '30%', 'price': 1440}]},
                                         'nom2m': {'delovoj': [{'speed': '4M', 'discount': '30%', 'price': 2000},
                                                               {'speed': '6M', 'discount': '30%', 'price': 3000},
                                                               {'speed': '8M', 'discount': '30%', 'price': 4000},
                                                               {'speed': '10M', 'discount': '30%', 'price': 5000}]}}},
    'khab':
        {
            'opt': {'yesm2m': {'m2mkontrol': [{'speed': '128k', 'discount': '30%', 'price': 180},
                                                                {'speed': '256k', 'discount': '30%', 'price': 240},
                                                                {'speed': '512k', 'discount': '30%', 'price': 300},
                                                                {'speed': '1M', 'discount': '30%', 'price': 480},
                                                                {'speed': '2M', 'discount': '30%', 'price': 720},
                                                                {'speed': '4M', 'discount': '30%', 'price': 960},
                                                                {'speed': '5M', 'discount': '30%', 'price': 1200}]},
                                      'nom2m': {'skorost': [{'speed': '30M', 'discount': '30%', 'price': 3000},
                                                            {'speed': '40M', 'discount': '30%', 'price': 4200},
                                                            {'speed': '50M', 'discount': '30%', 'price': 5900},
                                                            {'speed': '70M', 'discount': '30%', 'price': 8300},
                                                            {'speed': '100M', 'discount': '30%', 'price': 11700},
                                                            {'speed': '120M', 'discount': '30%', 'price': 16300},
                                                            {'speed': '150M', 'discount': '30%', 'price': 22800},
                                                            {'speed': '200M', 'discount': '30%', 'price': 31900},
                                                            {'speed': '250M', 'discount': '30%', 'price': 44700},
                                                            {'speed': '300M', 'discount': '30%', 'price': 62600}],
                                                'ozhn': [{'speed': '30M', 'discount': 0, 'price': 1300},
                                                         {'speed': '50M', 'discount': 0, 'price': 2500},
                                                         {'speed': '100M', 'discount': 0, 'price': 5000}],
                                                'uskorenie': [{'speed': '50M', 'discount': 0, 'price': 3500},
                                                              {'speed': '100M', 'discount': 0, 'price': 7000},
                                                              {'speed': '150M', 'discount': 0, 'price': 13000}]}},
                              'med': {'yesm2m': {'m2mkontrol': [{'speed': '128k', 'discount': '30%', 'price': 180},
                                                                {'speed': '256k', 'discount': '30%', 'price': 240},
                                                                {'speed': '512k', 'discount': '30%', 'price': 300},
                                                                {'speed': '1M', 'discount': '30%', 'price': 480},
                                                                {'speed': '2M', 'discount': '30%', 'price': 720},
                                                                {'speed': '4M', 'discount': '30%', 'price': 960},
                                                                {'speed': '5M', 'discount': '30%', 'price': 1200}]},
                                      'nom2m': {'delovoj': [{'speed': '4M', 'discount': '30%', 'price': 1500},
                                                            {'speed': '6M', 'discount': '30%', 'price': 2000},
                                                            {'speed': '8M', 'discount': '30%', 'price': 3000},
                                                            {'speed': '10M', 'discount': '30%', 'price': 4000}]}}}
}


