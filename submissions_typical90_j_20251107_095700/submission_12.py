# インデックスエラー,入力形式依存(短すぎるゴルフコード)
(n,),*L=[map(int,o.split())for o in open(0)];a=[0];b=[0]
for c,p in L[:n]:a+=a[-1]+p*(c<2),;b+=b[-1]+p*~-c,
for l,r in L[n+2:]:print(a[r]-a[l-1],b[r]-b[l-1])