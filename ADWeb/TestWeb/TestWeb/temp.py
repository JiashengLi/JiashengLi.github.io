def toXbioDemo(request):  # xbio-demo界面的动态生成,只在点击XBIO页面触发！！！
    tablecode = '<div class="row">'
    context = {}
    json_bioList = request.POST.getlist('bioList')
    if len(json_bioList) == 0:
        json_bioList = request.POST.getlist('bioList')
    elif len(json_bioList) != 0:
        json_bioList =json.loads(json_bioList[0])

        cardsPerPage = 9  # 每页页数
        biolist_data = (json_bioList["data"])  # type:LIST
        # print("data:",biolist_data)
        count = json_bioList["count"]
        # print("data子项:", (biolist_data[0])["casNo"])
        # 1.根据count总数，计算需要展示的页数（总个数/每页展示页数）向上取整。
        currentpageCount = 1 + (count // cardsPerPage)
        #print('%s是总数除以%s每页个数,计算后总数是%s页'%(count,cardsPerPage,currentpageCount))
        #print("数值：",biolist_data)
        # 3.通过索引将字典（biolist）的value值写入card中。
        #print(json_bioList)
        for i in range(0, cardsPerPage):
            card = '''<div class="panel panel-default col-md-4">'  # card 是每个分子卡片的代码
                           <div class="row">
                                  <div class="col-md-6 ">
                                      <div class="img-box">
                                     <img src="/static/images/XBIOAD.png" alt="">
                                     </div>
                                  </div>
                                  <div class="col-md-6 about-text-container">
                                      <div class="detail-box">
                                        <p class="about-p" >分子式</p>
                                        <p class="about-p" style="font-size:small !important;">cas号:%s</p>
                                        <p class="about-p" style="font-size:small !important;">货号：货号</p>
                                        <a href="https://www.xcessbio.com/">信息：infor</a>
                                      </div>
                                  </div>
                           </div>
                     </div>'''%((biolist_data[i])["casNo"])
            tablecode = tablecode + card  # 循环生成打印当前页的卡片
        tablecode = tablecode + '</div> '
        print(tablecode)
        # 第二个row开始
        # tablecode = tablecode + '<div class="row">'
        # pagination = '                <ul class="pagination pagination-lg">'
        # pagination = pagination + '       <li><a href="#">&laquo;</a></li>'
        # pagination = pagination + '       <li><a href="#">1</a></li>'
        # pagination = pagination + '       <li><a href="#">2</a></li>'
        # pagination = pagination + '       <li><a href="#">3</a></li>'
        # pagination = pagination + '       <li><a href="#">4</a></li>'
        # pagination = pagination + '       <li><a href="#">5</a></li>'
        # pagination = pagination + '       <li><a href="#">&raquo;</a></li>'
        # pagination = pagination + '   </ul>'
        #
        # tablecode = tablecode + pagination
        # tablecode = tablecode + '</div>'
        context['table'] = tablecode
        return render(request, 'xbio-demo.html', {'demotable': context['table']})

        # print(context['table'])
        # print(pagination)
    context['table'] = tablecode
    return render(request, 'xbio-demo.html', {'demotable': context['table']})