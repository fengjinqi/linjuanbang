<template>
	<view>
		<view class="tabs">
			<scroll-view class="scroll-view_H scroll-h" scroll-x="true" show-scrollbar="false" >
				<view class="nav-header uni-tab-item " v-if="category.length>0">
					<text :class="[{ active: active==index },'uni-tab-item-title']" v-for="(item,index) in category" :key='index' @click="getList(item.pid,index)">{{item.name}}</text>
				</view>
			</scroll-view>
		 </view>
		 <scroll-view scroll-y="true" @scroll="scroll" :scroll-top="scrollTop" :style="{height:height}" @scrolltolower='getHomePage'>
		 	<view class="">
		 		<swiper class="swiper" style="height: 90px;" circular ='true'>
		 			<swiper-item style="height: 90px;" v-if="banner.length>0" v-for="(item,index) in banner" :key='index'>
		 				<view class="swiper-item uni-bg-red" @click="navigator(item.url)" style="height: 90px;">
		 						<image class="img"  :src="item.img" style="height: 90px;" mode="scaleToFill"></image>
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
		 					<text class="price">劵后价:<text style="font-weight: bold;">{{tudu(item.priceInfo.price,item.couponInfo.couponList[0].discount)}}</text></text>
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
				return (sys.windowHeight-80)+'px'
			}
		},
		components:{
			uniLoadMore
		},
		created() {
			this.getBanner()
			uni.request({
				url:'https://m.fengjinqi.com/jd/category',
				method:'GET',
				success: (res) => {
					this.category = res.data[0]
					this.squared = res.data[1]
				}
			})
			this.getList(22,0)
		},
		methods:{
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
			getList(type,index){
				this.active = index
				uni.showLoading({
				    title: '加载中...'
				});
				this.page=1
				this.scrollTop = this.old.scrollTop
				this.$nextTick(function() {
					this.scrollTop = 0
				});
				this.categoryId = type
				uni.request({
					url:'https://m.fengjinqi.com/jd/getList',
					data:{'type':type},
					method:'GET',
					success: (res) => {
						uni.hideLoading()
						let result = res.data.jd_union_open_goods_jingfen_query_response
						this.msg = JSON.parse(result.result).data
						console.log(JSON.parse(result.result).totalCount)
						this.count = Math.ceil(JSON.parse(result.result).totalCount/20)
					}
				})
			},
			navigator(e){
				window.location.href=e
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
							console.log(item)
							
								this.msg = this.msg.concat(item)
						
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
@import '../static/css/comm.css';
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
