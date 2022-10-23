// pages/page_1/page_1.js
Page({
  /**
   * 页面的初始数据
   */
  data: {
    input_value: "",
    name_rank:{"清华大学":1,"北京大学":2,"浙江大学":3,"上海交通大学":4,"南京大学":5,"复旦大学":6,"中国科学技术大学":7,"华中科技大学":8,"武汉大学":9,"中山大学":10,"西安交通大学":11,"哈尔滨工业大学":12,"北京航空航天大学":13,"北京师范大学":14,"同济大学":15,"四川大学":16,"东南大学":17,"中国人民大学":18,"南开大学":19,"北京理工大学":20,"天津大学":21,"山东大学":22,"厦门大学":23,"吉林大学":24,"华南理工大学":25,"中南大学":26,"大连理工大学":27,"西北工业大学":28,"华东师范大学":29,"中国农业大学":30}
  },
  come_2(){
    wx.redirectTo({
      url: '/pages/page_2/page_2',
    })
  },
  come_3(){
    wx.redirectTo({
      url: '/pages/page_3/page_3',
    })
  },
  after(){
    wx.redirectTo({
      url: '/pages/page_2/page_2',
    })
  },
  getInputValue(e){
    this.setData({
      input_value: e.detail.value
    }) 
    // console.log(this.data.input_value)  //不能省略this.data
  },
  jump_university(e){
    console.log(e.currentTarget.dataset.postname)
    // console.log(this.data.name_rank[e.currentTarget.dataset.postname])
    // var url='../'+this.data.name_rank[e.currentTarget.dataset.postname]+'/'+this.data.name_rank[e.currentTarget.dataset.postname]
    // console.log(url)
    wx.navigateTo({
      url: '../search_school/search_school?name='+e.currentTarget.dataset.postname
    })
  },
  click_me(e){
    // console.log(e.currentTarget.dataset.postname)
    wx.navigateTo({
      url: '../'+this.data.name_rank[e.currentTarget.dataset.postname]+'/'+this.data.name_rank[e.currentTarget.dataset.postname]
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