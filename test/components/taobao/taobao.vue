<template>
	<view class="content">
		<view class="nav-header">
			<view class="status_bar">
				<navigator url="../search/search">
				<input type="text" disabled='true' placeholder ="搜索" placeholder-style='font-size:12px;text-align:center;' />
				</navigator>
			</view>
			<view class="tabs">     
				<scroll-view class="scroll-view_H scroll-h" scroll-x="true" show-scrollbar="false" >
					<view class="nav-header uni-tab-item " v-if="category.length>0">
						<text :class ="[{ active: active==1 },'uni-tab-item-title']" @click="getInit(category[0].comprehensive,1)">综合</text>
						<text :class ="[{ active: active==2 },'uni-tab-item-title']"  @click="getInit(category[0].shoe,2)">鞋包配饰</text>
						<text :class ="[{ active: active==3 },'uni-tab-item-title']"  @click="getInit(category[0].mother,3)">母婴</text>
						<text :class ="[{ active: active==4 },'uni-tab-item-title']"  @click="getInit(category[0].ladies,4)">女装</text>
						<text :class ="[{ active: active==5 },'uni-tab-item-title']"  @click="getInit(category[0].makeup,5)">美妆个护</text>
						<text :class ="[{ active: active==6 },'uni-tab-item-title']"  @click="getInit(category[0].food,6)">食品</text>
						<text :class ="[{ active: active==7 },'uni-tab-item-title']"  @click="getInit(category[0].mens,7)">男装</text>
						<text :class ="[{ active: active==8 },'uni-tab-item-title']"  @click="getInit(category[0].digita,8)">数码家电</text>
						<text :class ="[{ active: active==9 },'uni-tab-item-title']"  @click="getInit(category[0].underwear,9)">内衣</text>
						<text :class ="[{ active: active==10 },'uni-tab-item-title']"  @click="getInit(category[0].furnishing,10)">家居家装</text>
						<text :class ="[{ active: active==11 },'uni-tab-item-title']"  @click="getInit(category[0].sports,11)">运动户外</text>
					</view>
				</scroll-view>
			 </view>
		</view>
	
		
		
		<view class="">
			<scroll-view scroll-y="true" @scroll="scroll" :scroll-top="scrollTop" :style="{height:height}" @scrolltolower='getHomePage'>
				<swiper class="swiper"  circular ='true'>
					<swiper-item v-if="banner.length>0" v-for="(item,index) in banner" :key='index'>
						<view class="swiper-item uni-bg-red" @click="navigator(item.url)">
								<image :src="item.img" mode="scaleToFill"></image>
							</view>
					</swiper-item>
				</swiper>
				<view class="view">
					<view class="view-main" @click="navigator(item.coupon_share_url)" v-for="(item,index) in msg" :key='index' v-if="msg.length>0">
						<view class="view-img">
							<image :src="item.pict_url" mode="scaleToFill"></image>
						
						</view>
						<view class="view-footer">
							<text class="text">{{item.title}}</text>
							<view class="info">
								<text>原价:<text style="text-decoration: line-through;">¥{{item.zk_final_price}}</text></text>
								<text>销量:{{item.volume}}</text>
								
							</view>
							<view class="info">
								<text class="price">劵后价:<text style="font-weight: bold;">{{tudu(item.zk_final_price,item.coupon_amount)}}</text></text>
								<text class="juan">{{item.coupon_amount}}元劵</text>
							</view>
						</view>
					</view>
				</view>
				<uni-load-more :status="loading" v-show="type"></uni-load-more>
			</scroll-view>
		</view>
	</view>
</template>
<style scoped lang="scss">
	.nav-header{
		background: #ff464e;
		height: 86px;
		input{
		
		
		}
	}
  .status_bar {
     // height: var(--status-bar-height);
	  	padding: 5px;
		padding-top: 11px;
		input{
			border-radius: 20px;
			background: #fff;
			height: 30px;
			line-height: 30px;
		}
  }
 
  .scroll-h {
      width: 750upx;
      height: 80upx;
      flex-direction: row;
      /* #ifndef APP-PLUS */
      white-space: nowrap;
      /* #endif */
      /* flex-wrap: nowrap; */
      /* border-color: #cccccc;
  	border-bottom-style: solid;
  	border-bottom-width: 1px; */
  }
  
  .uni-tab-item {
      /* #ifndef APP-PLUS */
      display: inline-block;
      /* #endif */
      flex-wrap: nowrap;
   
  }
  
  .uni-tab-item-title {
	  /* #ifndef APP-PLUS */
	  display: inline-block;
	  /* #endif */
	  flex-wrap: nowrap;
	  padding-left: 24upx;
	  padding-right: 24upx;
      color: #fff;
      font-size: 14px;
      height: 80upx;
      line-height: 80upx;
      flex-wrap: nowrap;
      /* #ifndef APP-PLUS */
      white-space: nowrap;
      /* #endif */
	 &.active{
		 border-bottom: 2px solid #fff;
		 box-sizing: border-box;
		 font-weight: bold;
	 }
  }
  
  .uni-tab-item-title-active {
      color: #007AFF;
  }
  .swiper{
	  .swiper-item {
		  height: 150px;
		  width: 100%;
		  uni-image{
			  width: 100%;
		  }
		  image{
			  height: 150px;
		  }
	  }
  }
  .view{
	  display: flex;
	  flex-wrap: wrap;
	  justify-content: space-between;
	  padding: 0 10px;
	  .view-main{
		  width: 48%;
		  padding: 7px 0;
		  .view-img{
		  	height: 150px;
			width: 100%;
			image{
				width: 100%;
				height: 150px;
			}
		  }
		  .view-footer{
			   font-size: 13px;
			  .text{
				  font-size: 13px;
				  overflow: hidden;
				  text-overflow: ellipsis;
				  display: -webkit-box;
				  -webkit-line-clamp: 2;
				  -webkit-box-orient: vertical;
				  color: #323232;
				  margin-top: 5px;
			  }
			  .info{
				  display: flex;
				  justify-content: space-between;
				  color: #999;
				  margin-top: 5px;
				  .price{
					  color: #fb3434;
				  }
				  .juan{
					  padding: 2px 6px;
					  color: #fff;
					  background: linear-gradient(to left,#FF1F1F 0,#FBAA58 100%);
					  z-index: 1;
					  position: relative;
					  &:before{
						  position: absolute;
						      left: -4px;
						      top: 50%;
						      margin-top: -0.1875rem;
						      background: #fff;
						      display: block;
						      width: 0.375rem;
						      height: 0.375rem;
						      content: "";
						      border-radius: 0.625rem;
							  left: auto;
							      right: -4px;
					  }
					  &:after{
						      position: absolute;
						      left: -4px;
						      top: 50%;
						      margin-top: -0.1875rem;
						      background: #fff;
						      display: block;
						      width: 0.375rem;
						      height: 0.375rem;
						      content: "";
						      border-radius: 0.625rem;
					  }
				  }
				  
			  }
		  }
	  }
	  
  }
</style>
<script>
	import uniLoadMore from "@/components/uni-load-more.vue"
	export default {
		name:"taobao",
		data() {
			return {
				name:'',
				tabList:[],
				banner:[],
				category:[],
				msg:[],
				loading:'loading',
				type:false,
				page:1,
				flag:true,
				categoryId:'',
				scrollTop:0,
				active:1,
				old: {
					scrollTop: 0
				}
			}
		},
		components:{
			uniLoadMore,
		
		},
		computed:{
			tudu(){
				return function(a,b){
					return ((a*100-b*100)/100).toFixed(1)
				}
			},
			height(){
				var sys = uni.getSystemInfoSync();
				return (sys.windowHeight-125)+'px'
			}
		},
		created() {
			this.getBanner()
			this.getCategory()
			this.getInit()
		},
		methods: {
			getHomePage(e){
				if(!this.flag){
					return
				}
				this.flag=false
				this.type=true
				this.page++
				var _this = this
				uni.request({
					url:'/getHome',
					method:'GET',
					data:{"id":this.categoryId,'page':this.page},
					success:(res) => {
						this.flag=true
						this.type = false
						if(res.statusCode==200){
							
							if(res.data.tbk_dg_optimus_material_response.result_list.map_data.length>0){
						
								this.msg = this.msg.concat(res.data.tbk_dg_optimus_material_response.result_list.map_data)
						
							}else{
								this.type = true
								this.loading='noMore'
							}
						}else{
							uni.showToast({
							    title: '加载失败,请稍后重试',
								icon:'none'
							});
						}
					},
					fail: () => {
						this.flag=false
						this.type=false
						uni.showToast({
						    title: '网络错误,请稍后重试',
							icon:'none'
						});
					}
				})
			},
			getInit(e,n){
				this.page=1
				if(e){
					this.categoryId = e
					 this.scrollTop = this.old.scrollTop
					this.$nextTick(function() {
						this.scrollTop = 0
					});
					
				}
				if(n)this.active=n
				uni.showLoading({
				    title: '加载中...'
				});
				uni.request({
					url:'/getHome',
					method:'GET',
					data:{"id":e?e:''},
					success:(res) => {
						uni.hideLoading()
						if(res.statusCode==200){
							
							this.msg = res.data.tbk_dg_optimus_material_response.result_list.map_data
						}else{
							uni.showToast({
							    title: '加载失败,请稍后重试',
								icon:'none'
							});
						}
					},
					fail: () => {
						this.type=false
						uni.showToast({
						    title: '网络错误,请稍后重试',
							icon:'none'
						});
					}
				})
			},
			getBanner(){
				uni.showLoading({
				    title: '加载中...'
				});
				uni.request({
					url:'/banner',
					method:'GET',
					success: (res) => {
						uni.hideLoading()
						if(res.statusCode==200){
							this.banner=res.data
						}else{
							uni.showToast({
							    title: '加载失败,请稍后重试',
								icon:'none'
							});
						}
					},
					fail: (err) => {
						uni.showToast({
						    title: '网络错误,请稍后重试',
							icon:'none'
						});
					}
				})
			},
			getCategory(){
				uni.showLoading({
				    title: '加载中...'
				});
				uni.request({
					url:'/getCategory',
					method:'GET',
					success: (res) => {
						uni.hideLoading()
						if(res.statusCode==200){
							this.category = res.data
						}else{
							uni.showToast({
							    title: '加载失败,请稍后重试',
								icon:'none'
							});
						}
					},
					fail: (err) => {
						uni.showToast({
						    title: '网络错误,请稍后重试',
							icon:'none'
						});
					}
				})
			},
			navigator(e){
				window.location.href=e
			}
			,scroll(e){
				this.old.scrollTop = e.detail.scrollTop
			}
		}
	}
</script>
