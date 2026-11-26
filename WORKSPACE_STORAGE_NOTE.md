# 工作区精简说明

用户授权清理后，删除541个历史展开文件，共87,825,186字节（约87.8 MB / 83.8 MiB逻辑数据），沙箱du从约196 MiB降至111 MiB（后续小型研究增补会略有增长）。

删除前逐文件以SHA-256核验：全部内容在保留的历史交付ZIP中存在相同字节。没有改动ZIP、上传原件、V6/V7正文、当前longevity_new_territories或未匹配的源文献缓存。

归档化目录：corpus_engine_v1至v6、longevity_frontiers_round3、longevity_frontiers_round4。旧对话中指向这些展开目录的路径不再直接可用，但内容未丢失。

精确恢复映射：WORKSPACE_CLEANUP_RECEIPT.json，每条含原path、archive、member、sha256与bytes。恢复应使用映射中的ZIP成员内容写回原path，并校验SHA-256；不能假定所有文件与某一个ZIP具有同根结构。

保留当前成果两种形式（展开研究目录和最终ZIP）是为了继续研究与交付；本轮不再重复打包大附件。新研究只以小型增补目录推进。
