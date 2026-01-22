const assets = [
  {
    id: "1",
    name: "The Future of AI in SaaS - Episode 12",
    status: "Processed",
    type: "Video",
    date: "2 hours ago",
    clips: 8,
    thumbnail: "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=300&h=200&fit=crop"
  },
  {
    id: "2",
    name: "Product Strategy Deep Dive",
    status: "Processing",
    type: "Audio",
    date: "5 hours ago",
    clips: 0,
    thumbnail: "https://images.unsplash.com/photo-1614850523296-d8c1af93d400?w=300&h=200&fit=crop"
  },
  {
    id: "3",
    name: "Creator Economy Trends 2024",
    status: "Draft",
    type: "Video",
    date: "Yesterday",
    clips: 5,
    thumbnail: "https://images.unsplash.com/photo-1620641788421-7a1c342ea42e?w=300&h=200&fit=crop"
  }
];

export default function RecentAssets() {
  return (
    <div className="grid gap-4 md:grid-cols-2">
      {assets.map((asset) => (
        <div key={asset.id} className="flex overflow-hidden rounded-xl border border-slate-800 bg-slate-900/40">
          <div className="h-full w-32 flex-shrink-0">
            <img src={asset.thumbnail} alt="" className="h-full w-full object-cover opacity-80" />
          </div>
          <div className="flex flex-1 flex-col justify-center p-4">
            <div className="flex items-center justify-between">
              <span className={`text-[10px] font-bold uppercase tracking-wider px-2 py-0.5 rounded ${
                asset.status === 'Processing' ? 'bg-amber-500/10 text-amber-500 animate-pulse' : 'bg-emerald-500/10 text-emerald-500'
              }`}>
                {asset.status}
              </span>
              <span className="text-xs text-slate-500">{asset.date}</span>
            </div>
            <h4 className="mt-2 font-medium line-clamp-1 text-sm">{asset.name}</h4>
            <div className="mt-3 flex items-center text-xs text-slate-400">
              <span className="mr-3">{asset.type}</span>
              <span>{asset.clips} Clips generated</span>
            </div>
          </div>
        </div>
      ))}
    </div>
  );
}