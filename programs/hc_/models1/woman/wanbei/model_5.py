#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
__author__ = 'top'
date = '16/11/8'
我爱学习,学习使我快乐
'''
'''
长辈辈分	%(bf)s
年龄	%(nl)s
姓名	%(xm)s
举办地址	%(jbdz)s
//家庭住址	%(jtzz)s
晚辈辈分	%(fyrbf)s
//其他祝寿人姓名	%(qtxm)s
长辈名字	%(zbxm)s
季节	%(jj)s
'''

model_5 = [
    {
      "model":"%(bf)s把全部的爱给了儿女们，一人顶着这沉重的一片天。为了儿女们健康成长、成家立业，%(bf)s白天下地劳动，精打细算，操持家务，任劳任怨，把痛苦与困难留给自己，把快乐与方便让给儿女，使儿女们一个个成家立业，孙子、孙女们一个个长大成人。那个年代，是多么的艰难，多么的不易，%(bf)s受到了许多常人没有经受过的磨难，可%(bf)s无怨无悔，她为儿女们的高兴而高兴，为孙子们的成绩而骄傲。%(bf)s常教育子女要勤俭持家，诚实做人，实在办事，要我们好学上进，严以律己，努力工作，回报社会，报答家乡。她常教育我们要与人为善，好事多办，心要学长，路要修宽，特别是要多帮有困难的人，办实事、做好事。要堂堂正正做人。她能带头维护好家庭和乡党，邻居间的团结与和睦，乐于助人，逢人笑口常开，把困难留给自己，把方便让给别人。%(bf)s是位知足常乐的人，更是一个自得其乐的人，也富有幽默感。%(bf)s的一言一行，为我们晚辈树立了良好的学习榜样，她是儿女们的好妈妈，是儿媳们的好母亲。我是很爱我的%(bf)s，%(bf)s是一位伟大的母亲，又是一位伟大的%(bf)s。"
    },
    {
      "model":"在%(nl)s年的风雨中老人家寒心茹苦地将两子两女扶养成人，%(nl)s年风风雨雨，%(nl)s载生活苍桑。岁月的泪痕悄悄地爬上了他的额头，将老人家的双鬓染成白霜。大千世界里，孩子们把心中的话语都洒向老人那宽厚慈爱的胸膛。“严于律己，宽以待人，认真工作，发奋图强”简单的话语，让儿女镌刻在心，永记不忘。老人的辛苦并没有白费，在她的教育下，子女们都已经长大成人。老人赢得了无尚的荣光。现如今老寿星一家欢聚一堂，正可为儿子孝，儿媳能，女儿贤，女婿强。就连在校学习的孙女、外孙，外孙女们也是聪明伶俐，成绩优异，捷报频传，后继有人。让我们一起恭祝老寿星，福如东海，日月昌明。松鹤长春，春秋不老，古稀重新，欢乐远长。"
    },
    {
      "model":"风风雨雨%(nl)s年，我%(bf)s经历了太多的沧桑，太多的磨难，但她一生中积累的最大财富是他那勤劳善良的朴素品格，她那宽厚待人的处世之道，她那严爱有加的朴实家风。数十年来，%(bf)s把自己的心血和汗水都洒在了这块黄土地上，洒在了她充满艰辛坎坷的人生之路上。如今，%(bf)s已成了一位满头银发的老人，人生大部分的青春年华和宝贵时光都奉献给了儿女。在艰苦的生活条件下，%(bf)s为了晚辈的成家立业，她含辛茹苦，日夜操劳，不知耗费了多少心血和汗水！可以说，%(bf)s为了我们这个家，为了自己的子女及孙辈，奉献了一切！岁月的风霜早以消消地爬上了她的脸庞，也将她满头的青丝染成了白发，可以说%(bf)s饱尝了生活的酸甜苦辣，也见证了世间的人生百态。在这里，我们向%(bf)s由衷地说一声：%(bf)s，您坚强果敢的高尚品质永远是我们学习的榜样。"
    },
    {
      "model":"%(nl)s岁的%(bf)s，阅尽沧桑中积累的最大财富是他善良正直、诚实守信的为人品格，是她宽厚待人、宽广容人的处事之道，是她勤奋好学、孜孜不倦的上进之心，是她严爱有加、重亲重友的朴实家风。这一切，伴随着她经历了%(nl)s年的苦乐，更伴随她迎来了今后晚年生活的幸福，这一切也言传身教成为了我们子女们做人做事的标准，激励我们忠孝传代，团结和睦，开拓事业，不断进取。 "
    },
    {
      "model":"%(bf)s，%(nl)s岁是您生命的秋天，有着枫叶一般的色彩，%(nl)s年只是历史长河的短暂一瞬间，而您包容.博爱的精神，一直影响着我们的成长，您的坦荡磊落，正直做人的态度，一直引导着我们。对于我们来说，最大的幸福就是在一个良好的家庭环境下成长，而我们拥有了这种幸福，并一直伴随着我们，所以在您的生日，我们怀着一颗感恩的心，感谢您；我们怀着一颗感激之情，感谢您给予我们的关爱和培养，此时我们想再次向您说声“谢谢您，%(bf)s”。"
    },
    {
      "model":"%(bf)s，亲爱的%(bf)s！今天，我们当着众位亲朋好友的面，向您庄严承诺：我们一定以您为榜样，以更大的热情，更好的态度，更高的标准，更严的要求，造福社会，服务大众，孝敬老人，友爱朋友，和睦邻里，善处人际，严于律己，宽以待人，认真工作，发奋图强，%(bf)s教诲，永志不忘。"
    },
    {
      "model":"今天我的%(bf)s年以%(nl)s，再坐的各位能在远道而来还能为%(bf)s来过寿诞，实属感谢，你们是世上最幸福的人!%(nl)s是向心力凝聚力感召力集结力很给力。使家族近年相聚人员最全，感谢%(nl)s!%(nl)s给咱机会让新朋好友团圆，互叙衷肠实数天意，是快乐的家庭，幸福的家庭，美满的家庭，和-谐的家庭，长寿的家庭，可亲可爱可敬的一家人。让我们为他们祈祷祝福吧!老寿星十足走过了将近一个世纪的人生里程，老人阅尽了人间沧桑，饱偿了人间冷暖、品味了人生的酸甜苦辣世态炎凉，老人家晚年幸福生活密甜。她一生中积累的最大财富是那勤劳朴素和善良品格，豁达博爱的胸怀，知书答理的情怀，宽厚待人的处事之道，严爱有加的朴实家风，这一切伴随她经历了坎坷的岁月，才使得她缔造的李氏家族，治家有道，教子有方，家兴业旺，可谓人人出类拔萃、枝繁叶茂后继有人，真值得她老人家笑傲人生!岁月冉冉时不我待，伴她迎来了今天的晚年幸福%(nl)s岁寿诞。道一声老人家你辛苦了，寿诞快乐。"
    },
    {
      "model":"大家请往这里看,我们的老寿星她老人家看起来是慈眉善目，心装喜悦，宁静安详，精神饱满，红光满面、神采奕奕，身体健康。古人云，如今她老人家今天已经是%(nl)s高龄。这是老人最美好的时刻，也是人生最美好华章。老人是陈年的酒、老人是沉默的金，家有老人、乐享天伦、家有老人;幸福永存!让我们大家再一次把掌声响起来，乐队奏起来，鲜花献上来，向她老人家%(nl)s岁寿辰，表示热烈的祝贺!想想您的背影 ，我感受了坚韧 ，抚摸您的双手 ，我摸到了艰辛，不知不觉您鬓角露了白发，不声不响您眼角上添了皱纹，有老有小您手里捧着笑声，再苦再累您脸上挂着温馨 ，恐惧时你是一块踏脚的石，黑暗时你是一盏明亮的灯，枯竭时你是一湾生命的水，努力时你是精神上的支柱，成功时您又是鼓励与警钟，这个人是%(bf)s、伟大的%(bf)s! 常言说山中常有千年松，世间难逢百岁人，能够和老人一起度过这美好的时光能为老寿星生日作主持，真是三生有幸，感谢家族的信任，今天能够参加这样的生日寿宴的各位也可以说是有幸今生。"
    },
    {
      "model":"在%(nl)s年的风雨中，%(bf)s含辛茹苦的将她的子女抚养成人。%(nl)s年的风风雨雨，%(nl)s载生活沧桑。岁月的泪痕悄悄的爬上了他的额头，将老人家的双鬓染成白霜。大千世界里，孩子们把心中的话语都撒向老人那宽厚慈爱的胸膛。“严于律己，宽以待人，认真工作，发奋图强”简单的话语，让儿女镌刻在心，永记不忘。老人的辛苦并没有白费，在他的教育下，子女们都已经长大成人，为老人赢得了无尚的荣光。她的儿女已经成为名候一方的成功人士。先如今老寿星一家四世同堂，正可谓儿子孝，儿媳能，女儿贤，女婿强。让我们一起恭祝老寿星，福如东海，日月昌明。松鹤长春，春秋不老，古稀重新，欢乐远长。"
    },
    {
      "model":"%(nl)s年来，%(bf)s一同陪伴着我们成长。%(nl)s年风风雨雨，%(nl)s载生活苍桑。岁月的痕迹已经驻足%(bf)s的额头，将%(bf)s的双鬓染白。 “严以律己，宽以待人，认真学习，勤奋工作”是%(bf)s对我们经常的教诲。我们都已经长大成人，成家立业，在各自的工作岗位上做出了一定成绩，这也是我们送给%(bf)s最好的礼物。现在，全家三世同堂，正可谓儿子孝，儿媳贤，女儿良，女婿强。孙辈们也个个是品质优秀、聪慧伶俐。儿孙们的快乐和幸福已成为父母最大的快乐和幸福，我们为有这样的%(nl)s感到骄傲和自豪。"
    },
  ]