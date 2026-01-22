import { Video, Scissors, Share2, MousePointerClick } from "lucide-react";

const stats = [
  { name: "Total Master Assets", value: "42", icon: Video, color: "text-blue-500" },
  { name: "Derived Clips", value: "184", icon: Scissors, color: "text-purple-500" },
  { name: "Scheduled Posts", value: "12", icon: Share2, color: "text-amber-500" },
  { name: "Avg. Engagement", value: "+24%", icon: MousePointerClick, color: "text-emerald-500" },
];

export default function StatsCards() {
  return (
    <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
      {stats.map((stat) => (
        <div key={stat.name} className="rounded-xl border border-slate-800 bg-slate-900 p-6">
          <div className="flex items-center justify-between">
            <stat.icon className={`h-5 w-5 ${stat.color}`} />
          </div>
          <div className="mt-4">
            <p className="text-sm font-medium text-slate-400">{stat.name}</p>
            <p className="text-2xl font-bold">{stat.value}</p>
          </div>
        </div>
      ))}
    </div>
  );
}