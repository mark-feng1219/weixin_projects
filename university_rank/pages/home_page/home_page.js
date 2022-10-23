// pages/home_page/home_page.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    Title: "2020最新软科中国大学排名",
    text1: "大学成就梦想",
    text2: "欢迎查询",
    text3: "2020年软科大学排名"
  },

  onTapButton: function(){
    wx.navigateTo({
      url: '../page_1/page_1',
    })
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad(options) {

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