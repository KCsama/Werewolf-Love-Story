# script.rpy

#好感度设置
default affection = 0  # 初始好感度为 0


#游戏开始
label start:

    scene bg forest_road

    #序章
    jump chapter0
    
label chapter0_end:

    #第一章
    jump chapter1


label chapter1_end:

    "我到底在做什么？把一个来历不明的人带回家，真的安全吗？"

    "一边走，我一边感到不安。尽管他表现出无助的样子，但总觉得有什么事情隐藏在背后，我完全不知道自己将要面对什么。"
    
    "他跟在我身后，脚步沉重但又急促，仿佛随时会发生什么不好的事情。他的紧张情绪让我更加不安。"
    
    "空气似乎比平时更沉闷，原本熟悉的树林此刻却显得格外陌生，像是隐藏着什么不为人知的秘密。每走一步，我都在思考：这真的是一个正确的决定吗？"

    #第二章
    #jump chapter2



    return


