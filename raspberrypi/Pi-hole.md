# Pi-Hole


Ref URLs:
```
https://www.youtube.com/watch?v=gPkSPzKEHP4
```
```
https://www.youtube.com/watch?v=0wpn3rXTe0g
```

# hosts.oisd.nl

```
https://hosts.oisd.nl/
```

# The Firebog

```
https://raw.githubusercontent.com/PolishFiltersTeam/KADhosts/master/KADhosts.txt
https://raw.githubusercontent.com/FadeMind/hosts.extras/master/add.Spam/hosts
https://v.firebog.net/hosts/static/w3kbl.txt
https://raw.githubusercontent.com/matomo-org/referrer-spam-blacklist/master/spammers.txt
https://someonewhocares.org/hosts/zero/hosts
https://raw.githubusercontent.com/VeleSila/yhosts/master/hosts
https://winhelp2002.mvps.org/hosts.txt
https://v.firebog.net/hosts/neohostsbasic.txt
https://raw.githubusercontent.com/RooneyMcNibNug/pihole-stuff/master/SNAFU.txt
https://paulgb.github.io/BarbBlock/blacklists/hosts-file.txt
https://adaway.org/hosts.txt
https://v.firebog.net/hosts/AdguardDNS.txt
https://v.firebog.net/hosts/Admiral.txt
https://raw.githubusercontent.com/anudeepND/blacklist/master/adservers.txt
https://s3.amazonaws.com/lists.disconnect.me/simple_ad.txt
https://v.firebog.net/hosts/Easylist.txt
https://pgl.yoyo.org/adservers/serverlist.php?hostformat=hosts&showintro=0&mimetype=plaintext
https://raw.githubusercontent.com/FadeMind/hosts.extras/master/UncheckyAds/hosts
https://raw.githubusercontent.com/bigdargon/hostsVN/master/hosts
https://raw.githubusercontent.com/jdlingyu/ad-wars/master/hosts
https://v.firebog.net/hosts/Easyprivacy.txt
https://v.firebog.net/hosts/Prigent-Ads.txt
https://raw.githubusercontent.com/FadeMind/hosts.extras/master/add.2o7Net/hosts
https://raw.githubusercontent.com/crazy-max/WindowsSpyBlocker/master/data/hosts/spy.txt
https://hostfiles.frogeye.fr/firstparty-trackers-hosts.txt
https://hostfiles.frogeye.fr/multiparty-trackers-hosts.txt
https://www.github.developerdan.com/hosts/lists/ads-and-tracking-extended.txt
https://raw.githubusercontent.com/Perflyst/PiHoleBlocklist/master/android-tracking.txt
https://raw.githubusercontent.com/Perflyst/PiHoleBlocklist/master/SmartTV.txt
https://raw.githubusercontent.com/Perflyst/PiHoleBlocklist/master/AmazonFireTV.txt
https://gitlab.com/quidsup/notrack-blocklists/raw/master/notrack-blocklist.txt
https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Alternate%20versions%20Anti-Malware%20List/AntiMalwareHosts.txt
https://osint.digitalside.it/Threat-Intel/lists/latestdomains.txt
https://s3.amazonaws.com/lists.disconnect.me/simple_malvertising.txt
https://v.firebog.net/hosts/Prigent-Crypto.txt
https://raw.githubusercontent.com/FadeMind/hosts.extras/master/add.Risk/hosts
https://bitbucket.org/ethanr/dns-blacklists/raw/8575c9f96e5b4a1308f2f12394abd86d0927a4a0/bad_lists/Mandiant_APT1_Report_Appendix_D.txt
https://phishing.army/download/phishing_army_blocklist_extended.txt
https://gitlab.com/quidsup/notrack-blocklists/raw/master/notrack-malware.txt
https://raw.githubusercontent.com/Spam404/lists/master/main-blacklist.txt
https://raw.githubusercontent.com/Te-k/stalkerware-indicators/master/generated/hosts
https://urlhaus.abuse.ch/downloads/hostfile/
https://v.firebog.net/hosts/Prigent-Malware.txt
https://v.firebog.net/hosts/Shalla-mal.txt
https://zerodot1.gitlab.io/CoinBlockerLists/hosts_browser
https://raw.githubusercontent.com/chadmayfield/my-pihole-blocklists/master/lists/pi_blocklist_porn_top1m.list
https://v.firebog.net/hosts/Prigent-Adult.txt
https://raw.githubusercontent.com/anudeepND/blacklist/master/facebook.txt
```



# Blacklist management

Ref URL: https://discourse.pi-hole.net/t/collection-of-regex-for-blacklisting/43178

Blacklists:
```
^(.*\.)*(sonobi|contentabc|exponential|bebi|3lift|leanplum|hotjar|m-pathy|parsely|exelator|touchcommerce|magnetic|exosrv|go2affise|mgid|clksite|tynt|inclk|bidswitch|optimizely|tiqcdn|maxymiser|9xiazaiqi|siquality|snwxn|8wix|tudown|psdzy|bankofamericaslpemr|cloudns|pfa.levexis)\.([a-z]{2,3}\.)*[a-z]{2,6}$

^(.*\.)*(dotomi|urbanairship|criteo|yimg|footprint|sitescout|turn|w55c|openx|voluumtrk|videoplaza|inmobi|reporo|cnzz|skim(resources|links)|tribalfusion|getsocial|hoverr|mediaplex|auditude|tacoda|puserving|d(e|o)mdex)\.([a-z]{2,3}\.)*[a-z]{2,6}$

^(.*\.)*(buffpanel|redshell|treasuredata|unity(ads|3d)|evidon|flashtalking|mathtag|mediamath|scorecardresearch|yieldmanager|sharezips|liveadvert|mktoresp|online-metrix|mobileapptracking|webengage|mpstat|trafficjunky|alphonso|stickyadstv|marketo|tubemogul|kameleoon|24s|0x1f4b0)\.([a-z]{2,3}\.)*[a-z]{2,6}$

^(.*\.)*(petametrics|localytics|onthe|newrelic|casalemedia|tidaltv|newsinc|nr-data|tapad|crazyegg|vserv|solocpm|ojrq|getclicky|narrative|7eer|evyy|impactradius|redtrack|content-ad|sharethrough|getui|pro-market|albacross|evergage|araleg|districtm|singular|dynamicyield|smrtb|everesttech|snapchatprime)\.([a-z]{2,3}\.)*[a-z]{2,6}$

^(.*\.)*(perimeterx|coremetrics|veinteractive|netcoresmartech|vungle|batmobi|marinsm|igexin|keywordblocks|facebook-info|freecontent|hostingcloud|360safe|axiatraders|beginads|ero-advertising|inteleksys|joodfbnm*[0-9]*|nbrwer*[0-9]*|usergrid|trackersimulator|tapjoy|supercell|bluekai|chartboost|atues|duilawyeryork|bannerflow|bmmetrix|flagcounter)\.([a-z]{2,3}\.)*[a-z]{2,6}$

^(.*\.)*(segment|braze|amplitude|emetriq|buysellads|ioam|ensighten|eulerian|dnsdelegation|clicktale|samsungads|userlike|summerhamster|sourcepoint|adobetm|pcapredict|syscation|infosupports|arrowservice|bigdepression|earthsolution|firefoxupdata|infobusinessus|yahoodaily|newsonet|worthhummer|purpledaily|blackcake|msnhome)\.([a-z]{2,3}\.)*[a-z]{2,6}$

^(.*\.)*(inmobicdn|jizzads|leadbolt|nexage|milleniamedia|mobfox|mobilityware|newrelic|propellerads|revd(depo|sci)|segment|serving-sys|sharethis|startapp|steelhousemedia|tapjoy|viglink|webterren|adtaily|zedo|liadm|exposebox|jazdoxthxiv|jwmwtcmexc|thetradedesk||rocketfuel|ignitionone|komoot|squarelovin|cookiebot)\.([a-z]{2,3}\.)*[a-z]{2,6}$

^(.*\.)*(aatkit|abtasty|acce(ngage|sstrade)|adtec(h|jp|us)|anthill|atdmt|avazutracking|bfmino|bounceexchange|branch|clever(push|tap)|conviva|crittercism|cxense|deltadna|duapps|fractionalmedia|fyber|hyprmx|justpremium|lijit|mobileapptracking|ogury|omniture|presage|tapad|pubmatic|pushwoosh|qq|servedbyopenx|supersoni(c|cads)|swrve|webtrekk|aimatch|sas)\.([a-z]{2,3}\.)*[a-z]{2,6}$

^(.*\.)*(actioniq|hs-(analytics|banner)|hsleadflows|hubspot|agileone|bizible|crazyegg|acquia|wistia|engagio|lytics|am15|bannerbank|bbelements|bravenet|cedexis-radar|crypto-loot|economicoutlook|esomniture|estat|extreme-dm|ezcybersearch|fastclick|focalink|gemius|hyperbanner|iovation|kaffnet|yieldlove|histats|forsee)\.([a-z]{2,3}\.)*[a-z]{2,6}$

^(.*\.)*(indexww|yieldlove-ad-serving|xplosion|digitru|upapi|spotxchange|permutive|onesignal|usabilla|contextweb|ml314|afcpatrk|(klclick[0-9])|aidata|hybrid|deployads|perfectaudience|liveramp|didomi|etahub|giraff|hurra|sizmek|nativo|djaxadserver|webmasterplan|ggpht|zanox|audrte|agkn|dataxu|scarabresearch|ekomi)\.([a-z]{2,3}\.)*[a-z]{2,6}$

^(.*\.)*(apsalar|tune|qualtrics|neustar|webtrends|linksynergy|backtrace|doubleverify|ligatus|a4|rayjump|umeng|umengcloud|wootric|medialytics|herokuapp|yllix|mobpartner|combango|bugsense|burstly|count|crashlytics|do-not-tracker|eviltracker|getexceptional|jumptap|playtomic|stathat|163|206ads|2mdnsys|360in|4seeresults|accesstrade|ads[0-9]-adnow|pop(ads|cash)|popadscdn)\.([a-z]{2,3}\.)*[a-z]{2,6}$

^(.*\.)*(urekamedia|kochava|upsight|marfeel(cache|cdn|rev|tenmax)|blueseed|adx[0-9]|zucks|o-s|aralego|breaktime|mdotm|juicer|cnt|ematicsolutions|alcmpn|powerlinks|33across|1rx|bfmio|bnmla|doublepimp|weborama|specific(click|media)|acuityplatform|cnnx|scanscout|nxtck|socdm|simpleanalytics|gumgum|marketolive|demandbase|izooto|ibillboard)\.([a-z]{2,3}\.)*[a-z]{2,6}$

^(.*\.)*(invitemedia|microad|ardata|152media|exoclick|doublemax|wywy|navdmp|trafficstars|pubexchange|vdopia|lsosad|aaxads|mantisadnetwork|triplelift|trafficfactory|themoneytizer|insurads|proads|pxlad|flux-adserve|eclick|vcmedia|nova(net|onads|on|nox)|coccoc|polyad|cleverads|ambient-platform|mangoads|cityads|autoads|yoads)\.([a-z]{2,3}\.)*[a-z]{2,6}$

^(.*\.)*(oewabox|metriweb|caramb(o|ola)|refinedads|klaviyo|a-mo|fieldtest|justuno|smartredirect|ezoic|statscrop|optinmonster|nr-data|avocet|bttrack|eyeota|jetlore|1up|abmr|acxiom-online|mlnadvertising|amgdgt|askmen|bam-x|bidr|bluecava|brand-display|brilig|ccgateway|channelintelligence|choicestream|clickagy|cognitivlabs|collective-media)\.([a-z]{2,3}\.)*[a-z]{2,6}$

^(.*\.)*(company-target|crosspixel|crsspxl|decdna|decideinteractive|disqus|emxdgt|extremetech|eyeviewads|btbuckets|fetchback|fimserve|freeskreen|gmads|gwallet|hlserve|imiclk|innovid|insidecrm|intentmedia|interclick|ipr(edictive|omote)|iqm|kargo|knorex|lkqd|logicbuy|marchex|media6degrees|mediaforge|mediaiqdigital|mixpo|mmismm|numberly|1000mercis)\.([a-z]{2,3}\.)*[a-z]{2,6}$

^(.*\.)*(mxptint|ncaudienceexchange|net(mng|seer)|owneriq|parrable|pm14|postrelease|pro-market|raasnet|retargetly|revsci|rfihub|rkdms|ru4|samba|semasio|sojern|udmserve|unrulymedia|vindicosuite|vmmpxl|vmweb|wsod|xad|xgraph|yieldmo|yieldoptimizer|youknowbest|zemanta|skimlinks|ipromote|lotame|contentsquare|matomo|piwik|roq|emerse|widespace)\.([a-z]{2,3}\.)*[a-z]{2,6}$

^(.*\.)*(nrich|rtbhouse|sovrn|beeswax|indexexchange|c3metrics|contactimpact|1plusx|semrush|improvedigital|xandr|madvertise|neural|rhythmone|inskinmedia|jivox|gsi-one|celtra|tapfiliate|req|moburst|webmechanix|divisionoflabor|commcreative|metrictheory|gkv|periscope|yieldbranding|gumas|fivebyfiveglobal|williamswhittle|baycreative|milleradagency)\.([a-z]{2,3}\.)*[a-z]{2,6}$

^(.*\.)*(farinella|wearesculpt|neonambition|envision-creative|tronviggroup|databricks|gotomarketers|maxaudience|perfectsearchmedia|titangrowth|3mediaweb|directom|seobrand|disruptiveadvertising|bigleap|silverbackstrategies|ignitevisibility|thriveagency|webfx|seoinc|socialseo|frac|klientboost|avalaunchmedia|siegemedia|straightnorth|gulosolutions|grafik)\.([a-z]{2,3}\.)*[a-z]{2,6}$

^(.*\.)*(thestorywebs|directiveconsulting|pbjmarketing|befoundonline|walkersandsdigital|firebellymarketing|comradeweb|contentbureau|hanapinmarketing|fruition|digitalbrandexpressions|noblestudios|thoughtspot|collibra|erne|uimserv|belboon)\.([a-z]{2,3}\.)*[a-z]{2,6}$

^(.*\.)*(app(boy|next|adhoc|celerator|ier|odeal|lovin|nexus|sflyer|boy|brain|ier|lvn|spot|timize|see|ads|lifier|lift|logrocket|-measurement|topia))\.([a-z]{2,3}\.)*[a-z]{2,6}$

^(.*\.)*(ad(j|skeeper|dtoany|vertica|true|vertnative|pushup|media|master|ledge|kernel|kmob|future|bro|booth|ap|apt|4game|just|telligent|4mat|tng|alliance|link|marketplace|[0-9]|adapted|acado|alliance|alyser|brite|bureau|and|blade|brodealsnetwork|spirit|epom|lightning|plugg|glare|speed|butler|x|roll|port|river|srvr|advisor|symptotic|dthis|rtx|scale))\.([a-z]{2,3}\.)*[a-z]{2,6}$

^(.*\.)*(ad(smogo|target|infuse|conversantmedia|now|view|ups|tim(a|aserver|ming)|srv|spruce|see|same|sniper|smoloco|shot|skeeper|x1|tdp|hese|lightning|micro|entifi|ventori|worx|zerk|roll|safeprotected|this|colony|tech[a-z]{1,2}|dthisedge|looxtracking|vertising|nxs|(ds|s)wizz|omik|k2x|k2|ition|this|form|ocean|protect|science|tlgc|vertserve|thrive))\.([a-z]{2,3}\.)*[a-z]{2,6}$

^(.*\.)*(ad(netasia|clixx|hacker|xcorp|vergine|optimize|grx|sfactor|snative|op|high|xxx|schoom|recover|spsp|safety|marvel|brix|servme|flex|rcdn|maym|pone|xadserv|up-tech|timaserver|network|tima|360|pia|sota|splay|sparc|legend|chemy|haven|ready|viva|gear|ikteev|dapptr|defend|ventureppc))\.([a-z]{2,3}\.)*[a-z]{2,6}$

^(.*\.)*(ad-(balancer|brix|center|cloud|delivery|delivery|locus|maven|move|plus|score|srv|stir))\.([a-z]{2,3}\.)*[a-z]{2,6}$
```

Whitelist:
```
^(.*\.)*(dpd|ups|dhl|safelinking|githubusercontent|researchintel|intel|github|foldingathome|sysctl|apple-dns|apple|icloud|windowsupdate|samsung(electronics|otn|acr|cloudsolution|qbe)|plex|office|msftncsi|microsoftonline|dropbox|pr0gramm|solvemedia|microsoft|tnt-digital|fedex|creative)\.([a-z]{2,3}\.)*[a-z]{2,6}$

Sites I learned from, and used to inspire me:

For checking a RegEx:

https://regex101.com/
https://regexr.com/
Tested and Maintained Regexs:

https://github.com/mmotti/pihole-regex
https://github.com/cbuijs/accomplist/blob/8f3946d58667e6d09951a994e839f297cae95e0e/chris/regex.black
https://github.com/nocturnalarchives/BlockLists
```

# Main List but in that just download and install everything.txt only
# Example Below.
`https://raw.githubusercontent.com/blocklistproject/Lists/master/everything.txt`

Main URL: `https://github.com/blocklistproject/Lists` 
