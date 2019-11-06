<template>
	<view class="content">
<!-- 		<taobao v-if="name.name=='淘宝'"></taobao>
		<j-d v-if="name.name=='京东'"></j-d>
		<wyg-bottom-tab tabIndex=1 :tabListParent="tabList" v-if="tabList.length>0"></wyg-bottom-tab> -->
	</view>

</template>

<script>
	import wygBottomTab from '@/components/wyg-bottom-tab/wyg-bottom-tab.vue';
	import taobao from '@/components/taobao/taobao.vue'
	import JD from '@/components/jd.vue'
	export default {
		data() {
			return {
				name:'',
				tabList:[],
			
			}
		},
		components:{
			wygBottomTab,
			taobao,
			JD
		},
		onLoad() {
			uni.request({
				url:'https://m.fengjinqi.com/getType',
				method:'GET',
				success: (res) => {
					this.tabList=res.data.map(item=>{
						 if(item.name=='淘宝'){
							item.imgOff='../../static/wyg-bottom-tab/img/taobao.png'
							item.imgOn='../../static/wyg-bottom-tab/img/taobaoactive.png'
						}else if(item.name=='京东'){
							item.imgOff='../../static/wyg-bottom-tab/img/jd.png'
							item.imgOn='../../static/wyg-bottom-tab/img/jdactive.png'
						}
						return item
					})
					this.name=this.tabList[0]
				}
			})
			
			var _this = this
			uni.$on('table',function(data){
				_this.name = data
			})
		},
	
	}
</script>
