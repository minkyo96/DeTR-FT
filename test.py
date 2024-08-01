from pycocotools.coco import COCO
import matplotlib.pyplot as plt

coco = COCO('/data/glusterfs/datasets/landslide/annotations/instances_train2017.json')

# 모든 카테고리 로드
cats = coco.loadCats(coco.getCatIds())
cat_names = [cat['name'] for cat in cats]
cat_ids = coco.getCatIds()

# 클래스별 객체 수 계산
cat_counts = {cat: 0 for cat in cat_names}

for cat_id, cat_name in zip(cat_ids, cat_names):
    ann_ids = coco.getAnnIds(catIds=cat_id)
    cat_counts[cat_name] = len(ann_ids)

# 결과 출력
for cat, count in cat_counts.items():
    print(f'{cat}: {count}개')

# 클래스 분포 시각화
plt.figure(figsize=(12, 8))
plt.barh(list(cat_counts.keys()), list(cat_counts.values()))
plt.xlabel('객체 수')
plt.ylabel('카테고리')
plt.title('COCO 데이터셋 클래스 분포')
plt.show()