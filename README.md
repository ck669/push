**从任何平台过来的朋友们请先阅读此说明**

# 每日早安推送给别人家的女朋友

这里有[更新说明](./UPGRADE.md)

## 使用说明

不想看文字的可以看下面的视频教程：

https://www.bilibili.com/video/BV1ke4y1o7Wd/

在我刚想构思这个教程怎么让不懂编程的朋友很快入门的时候，我考虑到：避免服务器搭建，避免定时任务，避免接触代码。在经历过各种思考后，觉得可以用 Github Actions 来白嫖。。你如果有一个自己的服务器可以参考[这里](#代码使用)运行代码。

效果如图。当然，文字是可以修改的。
<img src="https://user-images.githubusercontent.com/9566402/183242263-c93517a2-5377-435d-8386-8d47252c9e07.jpg" width="300px" />

首先，按图搜索，测试号，进来之后微信扫码登录！
![cf7dbd4502df44765ed3506f55caea5](https://user-images.githubusercontent.com/9566402/183242272-134e37e7-718d-42dd-9ed7-fca2810e94e6.png)

按图点击 Fork，创建到自己的仓库下！
<img width="1471" alt="image" src="https://user-images.githubusercontent.com/9566402/186087195-d1f2c124-1b59-4ea8-93dc-0b1e31a2e754.png">

按下图，创建模板，设置变量，把微信公众平台上的各种字符串按说明创建到 GitHub -> Settings -> Secrets -> Actions 中。
![71bf9d11a876d23ef0f0728645a8ba0](https://user-images.githubusercontent.com/9566402/183242301-fd6ab30e-bfe5-4245-b2a9-f690184db307.png)
![381e8ee4a7c5ec6b8c09719f2c7e486](https://user-images.githubusercontent.com/9566402/183242295-4dcf06bb-2083-4883-8745-0af753ca805c.png)
![48c60750cec7adc546e0ad99e3082b3](https://user-images.githubusercontent.com/9566402/183242320-18500adc-14e5-4522-a3ad-ae19cc4479bf.png)

文字来一遍

APP_ID: 公众平台 appID

APP_SECRET: 公众平台 appSecret

TEMPLATE_ID: 模板 ID

USER_ID: 接收人的 OpenID 多个用换行分隔

BIRTHDAY: 倒数日（原生日），换行分隔，见更新说明。格式如 05-20，1999-11-04 这种，农历就是 小林 r05-20

START_DATE: 正数日期，格式：2008-08-08

CITY: 城市，不要加市，准确到地级市。比如：北京、天津、广州、承德。

启用自己项目下的 Action！
![30a5b1b2b06ba4a40a3d8ef01652409](https://user-images.githubusercontent.com/9566402/183242334-9943c538-ba3d-4d01-8377-d040143b7560.png)

如果运行出现错误，按以下方法可以看到错误，在这里 issue 提问也可以，在小红书群里问也可以
![6b0da6f44e18c2bfd94910c377d13e6](https://user-images.githubusercontent.com/9566402/183242349-1aa5ada6-2ee7-4cf9-a542-4b2dad88b8fe.png)

启用后可以直接运行，看看女朋友的手机有没有收到推送吧！
这个定时任务是每天早晨8点推送，如果会编程的同学可以自己自定义一些东西～

图中的操作，除了各种英文字符串不一样，模板消息中的中文不一样，其他的应该都是一样的，不然程序跑不通的～

Github 的右上角可以点击 star 给我点鼓励吧亲

小红书/抖音上点点关注，点点赞，有什么好玩的东西可以at我，我来教你们做

ps. 有一些注意事项在此补充

1. 第一次登录微信公众平台测试号给的 app secret 是错误的，刷新一下页面即可
2. 生日的日期格式是：`05-20`，农历就是`r05-20`，纪念日的格式是 `2022-08-09`，请注意区分。城市请写到地级市，比如：`北京`，`广州`，`承德`
3. 变量中粘贴的各种英文字符串不要有空格，不要有换行，除了模板之外都没有换行
4. Github Actions 的定时任务，在 workflow 的定义是 `0 0 * * *`，是 UTC 时间的零点，北京时间的八点。但是由于 Github 同一时间任务太多，因此会有延迟
5. 我会偶尔优化一下代码，emm 但现在我自己在做一个完整的平台项目，想让大家更加便捷地上手

## 代码使用
如果你有一个自己的服务器，或是不会关机的电脑，可以通过如下方式使用代码。本项目使用Python3。

注意：以下步骤面向具有一定编程基础的同学，需要了解git和Python的基本使用。如果你是纯小白，建议参考上面的[教程](#使用说明)通过Github Actions来使用本项目。如果仍想尝试通过代码方式运行，请先安装好git和Python3，git的安装教程可参考[这里](https://www.liaoxuefeng.com/wiki/896043488029600/896067074338496)，Python3的安装可参考[这里](https://www.liaoxuefeng.com/wiki/1016959663602400/1016959856222624)。

1. 首先clone本仓库：

```bash
git clone https://github.com/rxrw/daily_morning.git
```

2. 安装依赖：

```bash
cd daily_morning

pip3 install -r requirements.txt
```

3. 根据示例完成配置文件`config.yaml`。 `app_id`、 `app_secret`、 `user_ids` 和 `template_id` 的配置可参考[使用说明](#使用说明)

4. 运行代码`timer.py`，即可实现每日定时发送：

```bash
python3 timer.py
```

附：当然，如果你有多个女朋友，你可以在微信公众平台上为她们设置不同的模板，并且为每个人分别建立一个配置文件，例如：`xiaomei.yaml` 和`xiaohong.yaml`（注意在配置时千万不要写错了`user_ids`）。然后同时运行两个服务：
```bash
python3 timer.py --cfg xiaomei.yaml &

python3 timer.py --cfg xiaohong.yaml &
```

## 版权相关

更新：2022.08.22

再更新一下，之前说的最火的那个视频的作者联系我了，我加以下这些限制协议不是因为这位作者，因为她确实有标明出处。只不过当时我的抖音号不叫这个名字，所以找不到罢了。。

(啊其实是因为有很多人在抖音上发我这个教程，但完全没有标出处，都说是自己男朋友给做的，我什么时候有那么多女朋友了请联系我让我认识一下)

当初做这个项目的时候，其实没有想到会被这么多人喜欢，因此没有加任何的开源协议、版权声明、代码加密等措施。说实在的，这个功能很简单，但是有朋友告诉我很多人都在用我的代码和教程去自己发抖音集赞，甚至还有人进行盈利骗钱的操作。让我比较心烦的是，大家给别人的视频点赞，然后跑过来问我怎么用，我？？？

因此，这个项目我会继续更新（本来都不打算更新了），首先更新协议如下：

1. 根据 Github [默认版权协议](https://docs.github.com/cn/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository#choosing-the-right-license)，在未发布开源许可协议时，遵循默认版权法，即任何人无法修改、复制本项目。但由于本项目使用说明解读，因此在 2022年8月22日23:00 之前对本项目的复制、修改不做严格限制。（收费除外）
2. **增加 [GPLv3](https://www.gnu.org/licenses/gpl-3.0.txt) 协议：凡使用本项目，其代码必须公开；如由此项目衍生的收费服务，必须提前告知终端用户此项目是可以免费获得及收费的理由；在本项目基础上 Fork、修改后的代码，必须采用 GPLv3 协议。此协议受全世界版权法律保护，本人保留对一切违反本协议行为诉诸法律的权力。**
3. **版权声明：凡是在世界范围内各平台（包括但不限于抖音、微博、小红书、Github、Gitee、微信公众平台、微信小程序、Youtube、Instagram、Twitter 等）使用本项目（包括但不限于展示、发布使用说明等）时，必须在明显的位置（内容、评论区等）表明出处（在已知账号的情况下，提及原作者；未知账号的情况下，展示本项目的地址）。**
4. 文件保护声明：如果复制、修改本项目，衍生后的项目可以添加本文件的内容，但禁止删除本文件中的任何内容。
