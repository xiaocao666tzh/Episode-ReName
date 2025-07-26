## [1.2.2-rc3] - 2025-07-26
### Chore
- 添加了更多平台的构建

## [1.2.2-rc2] - 2025-07-25
相较于 1.2.2
### Added
- name_format 支持 {group} {stream} {encode} 分别对应制作组/字幕组，流媒体，视频编码
- 加入 `--no_ncraws` 方法，默认为1不识别，0为识别
- 加入 `--allow_sp` 方法，识别SP文件，默认为0不识别，1为识别  
目前以VCB-Studio组的命名方式进行测试，重命名为 `[Nekomoe kissaten&VCB-Studio] Bokutachi wa Benkyou ga Dekinai [CM01][Ma10p_1080p][x265_flac].mkv -> S01E00 - CM01.mkv`  
- 加入 `--dry_run` 方法，模拟运行，不执行重命名，默认为0直接重命名，1为不执行重命名
- name_format 在保留对原有语法的支持下，新增支持Jinja2语法，比如我目前在用的 name_format `S{{season}}E{{ep}}{% if resolution %} - {{resolution}}{% endif %}{% if encode %}_{{encode}}{% endif %}{% if stream %}_{{stream}}{% endif %}{% if group %}_{{group}}{% endif %}`

### Fixed
- 兼容更多特殊字幕命名
- 兼容更多视频后缀