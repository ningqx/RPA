import re

def get_text(text):
    data_bili = re.search('date_bili=.*',text).group(0)
    if re.search('==漫画链接==',text,re.A|re.I):
        link_weibo = 'link_weibo='+(re.search('wblink=.*?\|',text).group(0)[:-1]).split('=')[1]
        link_bili = 'link_bili='+re.search('bmlink=.*?\}',text).group(0)[:-1].split('=')[1]
        text1 = re.sub(r'==漫画链接==','',text,re.A|re.I)   
        text1 = re.sub(r'\{.漫画链接.*\}.','',text1,re.A|re.I)       
        text1 = re.sub(r'date_bili=.*',data_bili+ r'\n|'+link_weibo+r'\n|'+link_bili,text1) 
        return text1
    else:
        return text
        

# text = "{{漫画页顶}}\n{{漫画信息框 \n|color=#C3CECA\n|title_weibo=且将新火试新茶，诗酒趁年华。 \n|title_bili=年终总结报告 \n|number=35\n|episode=现代篇  \n|date_weibo=2018-02-11\n|date_bili=2021-01-11 \n}}\n{{cquote|待补充|旁白}}\n'''年终总结报告'''是[[有兽焉]]漫画的第35话。它于2018年02月11日在微博正式发布，并于2021年1月11日在哔哩哔哩漫画与其他414话一并上线。\n==漫画链接==\t\n{{漫画链接|wblink=G2Efq24eu|bmlink=537237}}\n==概要==\t\n===回家===\n待补充\n===年终===\n待补充\n==出场==\n===角色===\n{{出场角色列表|35}}\t\n==你知道吗？==\n===文化参考===\n====标题化用====\n{{标题化用|且将新火试新茶，诗酒趁年华。|宋代|《望江南·超然台作》}}\n\n===设定===\n===轶事===\n==注释==\t\n{{notefoot}}\n==参考资料==\n{{reflist}}\n{{-}}\n{{漫画总导航}}"
# text2 = "{{漫画页顶}}\n{{漫画信息框 \n|color=#C3CECA\n|title_weibo=且将新火试新茶，诗酒趁年华。 \n|title_bili=年终总结报告 \n|number=35\n|episode=现代篇  \n|date_weibo=2018-02-11\n|date_bili=2021-01-11 \n}}\n{{cquote|待补充|旁白}}\n'''年终总结报告'''是[[有兽焉]]漫画的第35话。它于2018年02月11日在微博正式发布，并于2021年1月11日在哔哩哔哩漫画与其他414话一并上线。\n==概要==\t\n===回家===\n待补充\n===年终===\n待补充\n==出场==\n===角色===\n{{出场角色列表|35}}\t\n==你知道吗？==\n===文化参考===\n====标题化用====\n{{标题化用|且将新火试新茶，诗酒趁年华。|宋代|《望江南·超然台作》}}\n\n===设定===\n===轶事===\n==注释==\t\n{{notefoot}}\n==参考资料==\n{{reflist}}\n{{-}}\n{{漫画总导航}}"
# get_text(text)