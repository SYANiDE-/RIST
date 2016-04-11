# RIST
RIST Reputation Investigation Spawn Tool

Download current stable Windows binaries:
[W32 Binary package](https://github.com/SYANiDE-/RIST/blob/master/RIST_1.02.12312015.binary.w32.rar?raw=true)

Download current stable source:
[Python source package](https://github.com/SYANiDE-/RIST/blob/master/RIST_1.02.12312015.source.rar?raw=true)


**Changelog 1.02**
* Fixed Virustotal and ZScalerZulu not opening correct results pages on occasion
* Fixed threading issues; query-against-sources operations are now fully independent threads for true parallelism.   No blocking between operations.
* This Github page is opened in new tab at program startup;  two-fold benefits:  1. Ensures a browser is already open, 2. Easier tracking of updates and news/issues/announcements.


**Changelog 1.01**
* Added threading for parallelism between requests  (this will be extremely nice in future works)
* Created Github repo to centralize efforts
* IN IP sources:
  * Added IPVoid
  * Added WebHostingHero
  * Added Hetrix
* IN URL sources:
  * Fixed TrendMicro
  * Fixed Virustotal
  * Fixed URLVoid
  * Added IsItHacked
  * Added NortonSafeWeb
  * Added McAfeeSiteAdvisor
  * Added ZScalerZulu
