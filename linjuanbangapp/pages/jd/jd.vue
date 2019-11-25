<template>
	<view>
		<view class="tabs">
			<scroll-view class="scroll-view_H scroll-h" scroll-x="true" show-scrollbar="false" :style="ring!='other'?style:''">
				<view class="nav-header uni-tab-item " v-if="category.length>0">
					<text :class="[{ active: active==index },'uni-tab-item-title']" v-for="(item,index) in category" :key='index' @click="getList(item.pid,index)">{{item.name}}</text>
				</view>
			</scroll-view>
		 </view>
		 <scroll-view scroll-y="true" @scroll="scroll" :scroll-top="scrollTop" :style="{height:height}" @scrolltolower='getHomePage'>
		 	<view class="">
		 		<swiper class="swiper"  circular ='true' autoplay='true'>
		 			<swiper-item  v-if="banner.length>0" v-for="(item,index) in banner" :key='index'>
		 				<view class="swiper-item uni-bg-red" @click="navigator(item.url)" >
		 						<image class="img"  :src="item.img"  mode="scaleToFill"></image>
		 					</view>
		 			</swiper-item>
		 		</swiper>
				<view class="squared">
					<text class='squared-text' v-for="(item,index) in squared" :key='index' @click="getList(item.pid)">{{item.name}}</text>
				</view>	
		 	</view>
		 	<view class="view">
		 		<view class="view-main" @click="navigator(item.couponInfo.couponList.length?item.couponInfo.couponList[0].link:item.pinGouInfo.pingouUrl?item.pinGouInfo.pingouUrl:'https://'+item.materialUrl)" v-for="(item,index) in msg" :key='index' v-if="msg.length>0">
		 			<view class="view-img">
					
		 				<image class="img" :src="item.imageInfo.imageList[0].url" mode="scaleToFill"></image>
		 			
		 			</view>
		 			<view class="view-footer">
		 				<text class="text">{{item.skuName}}</text>
		 				<view class="info">
							<text style="background: #e1251b;color: #fff;padding: 0px 2px;border-radius: 2px;" v-show="item.owner=='g'">{{item.owner=='g'?'自营':''}}</text>
		 					<text v-if="item.couponInfo.couponList.length>0">原价:<text style="text-decoration: line-through;">¥{{item.priceInfo.price}}</text></text>
							<text v-else-if="item.pinGouInfo.pingouPrice">原价:<text style="text-decoration: line-through;">¥{{item.priceInfo.price}}</text></text>
							<text v-else style="color: #fb3434;font-weight: bold;">价格:<text>¥{{item.priceInfo.price}}</text></text>
		 				</view>

		 				<view class="info" v-if="item.couponInfo.couponList.length>0">
								
		 					<text class="price">劵后价:<text style="font-weight: bold;">{{item.youhui}}</text></text>
		 					<text class="juan" >{{item.couponInfo.couponList[0].discount}}元劵</text>
		 				</view>
						<view class="info" v-else-if="item.pinGouInfo.pingouPrice">
							<text>{{item.pinGouInfo.pingouTmCount}}人即可拼团</text>
							<text class="juan" >拼团购:{{item.pinGouInfo.pingouPrice}}</text>
						</view>
		 			</view>
		 		</view>
		 	</view>
		 	<uni-load-more :status="loading" v-show="type"></uni-load-more>
		 </scroll-view>
	</view>
</template>

<script>
	import uniLoadMore from "@/components/uni-load-more.vue"
	export default {
		data() {
			return {
				loading:'loading',
				type:false,
				banner:[],
				category:[],
				categoryId:22,
				scrollTop:0,
				active:0,
				squared:[],
				page:1,
				count:0,
				msg:[],
				flag:true,
				old: {
					scrollTop: 0
				},
				ring:null,
				style:{
					   height: '40px'
				}
			};
		},
		computed:{
			tudu(){
				return function(a,b){
					return ((a*100-b*100)/100).toFixed(1)
				}
			},
			height(){
				var sys = uni.getSystemInfoSync();
				return (sys.windowHeight-40)+'px'
			}
		},
		components:{
			uniLoadMore
		},
		onLoad() {
			switch(uni.getSystemInfoSync().platform){
			    case 'android':
			       console.log('运行Android上')
				   this.ring = 'android'
			       break;
			    case 'ios':
			       console.log('运行iOS上')
				   this.ring = 'ios'
			       break;
				case 'devtools':
					this.ring = 'devtools'
					break;
			    default:
					this.ring =uni.getSystemInfoSync().platform
			       console.log('运行在开发者工具上')
			       break;
			}
			this.getBanner()
			uni.request({
				url:'https://m.fengjinqi.com/jd/category',
				method:'GET',
				success: (res) => {
					this.category = res.data[0]
					this.squared = res.data[1]
				}
			})
			this.getList(22,0,true)
		},
		methods:{
			getjs(a,b){
				console.log(a,b)
				return ((a*100-b*100)/100).toFixed(1)
			},
			getBanner(){
				uni.request({
					url:'https://m.fengjinqi.com/jd/get_banner',
					method:'GET',
					success: (res) => {
						if(res.statusCode==200){
							this.banner=res.data
						}
					},
					fail: () => {
						uni.showToast({
						    title: '网络错误,请稍后重试',
							icon:'none'
						});
					}
				})
			},
			getList(type,index,n){
				this.active = index
				this.categoryId = type
				if(!n)uni.showLoading({
				    title: '加载中...'
				});
				this.page=1
				this.scrollTop = this.old.scrollTop
				this.$nextTick(function() {
					this.scrollTop = 0
				});
				
				uni.request({
					url:'https://m.fengjinqi.com/jd/getList',
					data:{'type':type},
					method:'GET',
					success: (res) => {
						uni.hideLoading()
						let result = res.data.jd_union_open_goods_jingfen_query_response
						let item = JSON.parse(result.result).data
						this.msg=item.map(data=>{
							
							if(data.couponInfo.couponList.length>0){
								
								data.youhui=this.getjs(data.priceInfo.price,data.couponInfo.couponList[0].discount)
							}
							return data
						})
						console.log(this.msg)
						this.count = Math.ceil(JSON.parse(result.result).totalCount/20)
					},
					fail: () => {
						uni.hideLoading()
						uni.showToast({
						    title: '网络错误,请稍后重试',
							icon:'none'
						});
					}
				})
			},
			navigator(e){
				if(this.ring == 'ios'||this.ring == 'android'){
					var item={
						url:e
					}
					uni.navigateTo({
					    url: '/pages/webview/webview?item='+ encodeURIComponent(JSON.stringify(item))
					});
				}else if(this.ring == 'devtools'){
					var item={
						url:e
					}
					uni.navigateTo({
					    url: '/pages/webview/webview?item='+ encodeURIComponent(JSON.stringify(item))
					});
				}
				else{
					window.location.href=e
				}
				
			},
			getHomePage(){
				console.log(this.count)
					this.type = true
				if(this.page>=this.count){
					this.loading='noMore'
					return
				}else{
					this.loading='loading'
				}
				if(!this.flag){
					return
				}
				this.flag=false
				
				this.page++
				uni.request({
					url:'https://m.fengjinqi.com/jd/getList',
					method:'GET',
					data:{"type":this.categoryId,'page':this.page},
					success:(res) => {
						this.flag=true
						this.type = false
						if(res.statusCode==200){
							let result = res.data.jd_union_open_goods_jingfen_query_response
							let item = JSON.parse(result.result).data
						
								let obj=item.map(data=>{
									
									if(data.couponInfo.couponList.length>0){
										
										data.youhui=this.getjs(data.priceInfo.price,data.couponInfo.couponList[0].discount)
									}
									return data
								})
								
								//this.count = Math.ceil(JSON.parse(result.result).totalCount/20)
								this.msg = this.msg.concat(obj)
						
						}else{
							uni.showToast({
							    title: '加载失败,请稍后重试',
								icon:'none'
							});
						}
					},
					fail: () => {
						this.flag=true
						this.type=false
						uni.showToast({
						    title: '网络错误,请稍后重试',
							icon:'none'
						});
					}
				})
					
			},
			scroll(e){
			this.old.scrollTop = e.detail.scrollTop
		}
		}
	}
</script>
<style>

</style>
<style lang="less">
//@import '../../static/css/comm.css';

.status_bar {
     // height: var(--status-bar-height);
	  	padding: 5px;
		padding-top: 11px;
		.input{
			border-radius: 20px;
			background: #fff;
			height: 30px;
			line-height: 30px;
		}
  }
 
  .scroll-h {
	  max-width: 600px;
	
	   font-size: 14px;
     // width: 750upx;
   
      //flex-direction: row;
      /* #ifndef APP-PLUS */
      //white-space: nowrap;
      /* #endif */
      /* flex-wrap: nowrap; */
      /* border-color: #cccccc;
  	border-bottom-style: solid;
  	border-bottom-width: 1px; */
  }
  
  .uni-tab-item {
      /* #ifndef APP-PLUS */
     // display: inline-block;
      /* #endif */
	  white-space: nowrap;
	      font-size: 14px;
		      height: 40px;
			  display: inline-block;
			  line-height: 40px;
		  overflow-x: auto;
      //flex-wrap: nowrap;
	    
   
  }
  
  .uni-tab-item-title {
	
	 
	 padding: 0 12px;
      color: #fff;
      font-size: 14px !important;
     display: inline-block;

	 &.active{
		 // border-bottom: 2px solid #fff;
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
  		/*  uni-image{
  			  width: 100%;
  		  } */
  		  .img{
  			  height: 150px;
  			  width: 100%;
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
  			.img{
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
  						    margin-top: -4px;
  						    background: #fff;
  						    display: block;
  						    width: 8px;
  						    height:8px;
  						      content: "";
  						      border-radius: 0.625rem;
  							  left: auto;
  							      right: -4px;
  					  }
  					  &:after{
  						      position: absolute;
  						      left: -4px;
  						      top: 50%;
  						     margin-top: -4px;
  						     background: #fff;
  						     display: block;
  						     width: 8px;
  						     height:8px;
  						      content: "";
  						      border-radius: 0.625rem;
  					  }
  				  }
  				  
  			  }
  		  }
  	  }
  	  
  }
  
  
	.tabs{
		background-color: #e1251b
	}
	.squared{
		display: flex;
		flex-wrap: wrap;
		justify-content: center;
		.squared-text{
			width: 33%;
			display: flex;
			justify-content: center;
			font-size: 14px;
		}
	}
	
</style>
