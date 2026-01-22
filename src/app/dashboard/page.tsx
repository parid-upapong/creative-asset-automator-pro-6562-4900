import StatsCards from "@/components/dashboard/StatsCards";
import RecentAssets from "@/components/dashboard/RecentAssets";
import { ArrowUpRight, PlusCircle } from "lucide-react";

export default function DashboardPage() {
  return (
    <div className="space-y-8">
      <div className="flex items-end justify-between">
        <div>
          <h1 className="text-3xl font-bold tracking-tight">Welcome back, Creator</h1>
          <p className="mt-2 text-slate-400">
            Your AI agents have processed 12 hours of video this week.
          </p>
        </div>
        <div className="hidden lg:block text-right">
          <p className="text-sm text-slate-500 font-medium">Platform Status</p>
          <div className="flex items-center text-emerald-400 text-sm mt-1">
            <span className="h-2 w-2 rounded-full bg-emerald-400 mr-2 animate-pulse"></span>
            AI Engine Operational
          </div>
        </div>
      </div>

      <StatsCards />

      <div className="grid gap-6 lg:grid-cols-3">
        <div className="lg:col-span-2 space-y-6">
          <div className="flex items-center justify-between">
            <h2 className="text-xl font-semibold">Master Assets</h2>
            <button className="text-sm text-indigo-400 hover:text-indigo-300 flex items-center">
              View all <ArrowUpRight className="ml-1 h-4 w-4" />
            </button>
          </div>
          <RecentAssets />
        </div>

        <div className="space-y-6">
          <h2 className="text-xl font-semibold">Quick Actions</h2>
          <div className="grid gap-4">
            <ActionCard 
              title="Upload Master Asset" 
              desc="Transform long video into clips"
              icon={<PlusCircle className="text-indigo-400" />}
            />
            <ActionCard 
              title="Brand Intelligence" 
              desc="Update your voice profile"
              icon={<PlusCircle className="text-emerald-400" />}
            />
          </div>
        </div>
      </div>
    </div>
  );
}

function ActionCard({ title, desc, icon }: { title: string, desc: string, icon: React.ReactNode }) {
  return (
    <div className="group cursor-pointer rounded-xl border border-slate-800 bg-slate-900/50 p-4 transition-hover hover:border-slate-700 hover:bg-slate-900">
      <div className="flex items-start justify-between">
        <div className="rounded-lg bg-slate-800 p-2 group-hover:scale-110 transition-transform">
          {icon}
        </div>
      </div>
      <h3 className="mt-4 font-medium">{title}</h3>
      <p className="mt-1 text-sm text-slate-500">{desc}</p>
    </div>
  );
}