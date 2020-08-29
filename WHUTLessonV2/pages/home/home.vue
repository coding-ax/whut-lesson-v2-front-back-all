<template>
	<view class="contain-box">
		<view class="back-pic"><image src="https://xgpax.top/whutv2imgs/lakesi.jpg" mode="widthFix"></image></view>
		<view class="bottom-list">
			<view class="show-buttons">
				<view class="box-show-item">
					<view class="infos"><image mode="widthFix" src="../../static/icon/student.png"></image></view>
					<input type="number" v-model="username" placeholder="请输入学号" maxlength="13" />
					<image class="icon" src="../../static/icon/del.png" mode="widthFix" @click="reset"></image>
				</view>
				<view class="box-show-item">
					<view class="infos"><image mode="widthFix" src="../../static/icon/password.png"></image></view>
					<input v-model="password" placeholder="请输入密码" :password="!isShow" />
					<image class="icon" mode="widthFix" src="../../static/icon/hide.png" v-show="!isShow" @click="changeShow"></image>
					<image class="icon" mode="widthFix" src="../../static/icon/hide_active.png" v-show="isShow" @click="changeShow"></image>
				</view>
			</view>
			<view class="submit-button">
				<button type="primary" @click="save2storage">保存</button>
				<button type="primary" @click="reset">重置</button>
			</view>
			<view class="show-info">
				<view class="show-title">同学,你好！</view>
				<view class="small-title">
					欢迎使用武汉理工大学课表V2（可离线）。请使用教务管理系统登录，如仍然提示密码错误，可能是由于密码难度低，需要前往教务管理网提高密码难度。
				</view>
			</view>
		</view>
	</view>
</template>

<script>
export default {
	data() {
		return {
			username: '',
			password: '',
			isShow: false
		};
	},
	methods: {
		save2storage() {
			console.log(this.username, this.password);
			uni.showLoading({
				title: '保存中'
			});
			uni.setStorageSync('username', this.username);
			uni.setStorageSync('password', this.password);
			uni.hideLoading();
			uni.showToast({
				title: '保存完成，前往‘课表’页面下拉刷新即可看到课表哦',
				icon: 'none'
			});
			setTimeout(() => {
				uni.switchTab({
					url: '/pages/index/index'
				});
			}, 1000);
		},
		reset() {
			uni.showModal({
				title: '要重置吗？',
				content: '确定的话，需要重新绑定账号哦!',
				success: res => {
					if (res.confirm) {
						uni.clearStorageSync();
						this.username = '';
						this.password = '';
					}
				}
			});
		},
		changeShow() {
			this.isShow = !this.isShow;
		}
	},
	onReady() {
		let username = uni.getStorageSync('username');
		let password = uni.getStorageSync('password');
		this.username = username;
		this.password = password;
	}
};
</script>

<style scoped>
/* 总体 */
.contain-box {
	width: 100%;
	height: 100vh;
	display: flex;
	flex-direction: column;
	background-color: #f5f5f5;
}
/* 图片 */
.back-pic {
	width: 100%;
}
.back-pic image {
	width: 100%;
	animation: linear yaobai 1s;
}
@keyframes uptotop {
	from {
		transform: translateY(200rpx);
		opacity: 0;
	}
	to {
		transform: translateY(0rpx);
		opacity: 1;
	}
}
@keyframes rot {
	from {
		transform: scale(0.5);
	}
	to {
		transform: scale(1);
	}
}
@keyframes yaobai {
	0% {
		transform: rotate(25deg);
	}
	25% {
		transform: rotate(-12deg);
	}
	50% {
		transform: rotate(0deg);
	}
	75% {
		transform: rotate(12deg);
	}
	100% {
		transform: rotate(0);
	}
}
/* 底部整体 */
.bottom-list {
	width: auto;
	background-color: #f5f5f5;
	border-radius: 30rpx 30rpx 0 0;
	position: relative;
	padding: 30rpx;
	top: -80rpx;
	display: flex;
	flex-direction: column;
	justify-content: center;
	align-items: center;
	animation: linear uptotop 1s;
}

/* 显示info栏目 */
.show-info {
	background-color: #ffffff;
	border-radius: 30rpx;
	box-shadow: 0rpx 10rpx 5rpx #808080;
	display: flex;
	flex-direction: column;
	text-align: left;
	margin-top: 40rpx;
	padding: 15rpx;
	animation: linear rot 1s;
}
.show-title {
	font-size: 40rpx;
	font-weight: 700;
	color: #f53b57;
}
.small-title {
	font-size: 30rpx;
	color: #808080;
}
/* 输入框处理 */
.show-buttons {
	margin-top: 40rpx;
	background-color: #ffffff;
	padding: 18rpx;
	display: flex;
	flex-direction: column;
	width: 70%;
	border-radius: 18px;
}
.box-show-item {
	display: flex;
	flex-direction: row;
	width: 100%;
	align-items: center;
}
.box-show-item image {
	width: 60rpx;
	height: 60rpx;
	margin: 5rpx;
}
.box-show-item input {
	/* width: calc(100%-130rpx); */
}
/* buttons */
.submit-button {
	display: flex;
	flex-direction: row;
	margin-top: 30rpx;
}
.submit-button > * {
	flex: 1;
	margin: 15rpx;
	background-color: #f78fb3;
}
</style>
