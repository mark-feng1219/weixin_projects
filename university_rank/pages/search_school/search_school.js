// pages/search_school/search_school.js
let json_data = require("../data/result")
Page({
  /**
   * 页面的初始数据
   */
  data: {
    rank:undefined,
    university:undefined,
    province:undefined,
    type:undefined,
    score:undefined,
    // result_array:undefined
  },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad(options) {
    var index = -1
    var result_array = json_data.resultList[0].objectArray  //这里不能用冒号:;而且result_array前面要加var
    for(var i=0;i<300;i++)
    {
      if(result_array[0]["学校名称"][i]==" "+options.name)  //json里大学字符串多了一个空格
      {
        index = i ;
        break;
      }
    }
    if(index == -1)
    {console.log("不在列表内")}
    else
    {
    this.setData({
      rank:result_array[0]["排名"][index],
      university:result_array[0]["学校名称"][index],
      province:result_array[0]["省份"][index],
      type:result_array[0]["类型"][index],
      score:result_array[0]["总分"][index]
    })
    }
    // console.log(this.data.result_array[0]["学校名称"][0])
  },
  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady() {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow() {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide() {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload() {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh() {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom() {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage() {

  }
})