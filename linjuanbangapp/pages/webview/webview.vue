<template>
	 <view>
	        <web-view :webview-styles="webviewStyles" :src="src"></web-view>
	   </view>
</template>

<script>
	export default {
		data() {
			return {
				webviewStyles: {
					progress: {
						color: '#007aff'
					}
				},
				src:null
			}
		},
		onLoad(option) {
	switch(uni.getSystemInfoSync().platform){
		case 'devtools':
			this.ring = 'devtools'
			this.src = option.item
			break;
	    default:
	       console.log('运行在开发者工具上')
		   this.src = JSON.parse(option.item).url
	       break;
	}
			console.log(option)
			
		},
		methods: {
			
		}
	}
</script>

<style>

</style>
