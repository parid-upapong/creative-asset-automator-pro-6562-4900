"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { 
  LayoutDashboard, 
  Video, 
  Layers, 
  Palette, 
  Settings, 
  Zap,
  ChevronLeft,
  Menu
} from "lucide-react";
import { useUIStore } from "@/lib/store";
import { cn } from "@/lib/utils";

const navigation = [
  { name: "Dashboard", href: "/dashboard", icon: LayoutDashboard },
  { name: "Master Assets", href: "/dashboard/assets", icon: Video },
  { name: "AI Workflows", href: "/dashboard/workflows", icon: Zap },
  { name: "Brand Kit", href: "/dashboard/brand", icon: Palette },
  { name: "Integrations", href: "/dashboard/integrations", icon: Layers },
  { name: "Settings", href: "/dashboard/settings", icon: Settings },
];

export default function Sidebar() {
  const pathname = usePathname();
  const { isSidebarOpen, toggleSidebar } = useUIStore();

  return (
    <aside
      className={cn(
        "relative z-40 flex flex-col border-r border-slate-800 bg-slate-900 transition-all duration-300 ease-in-out",
        isSidebarOpen ? "w-64" : "w-20"
      )}
    >
      <div className="flex h-16 items-center justify-between px-6">
        {isSidebarOpen && (
          <span className="text-xl font-bold tracking-tighter text-indigo-500">
            OVERLORD
          </span>
        )}
        <button 
          onClick={toggleSidebar}
          className="rounded-lg p-1.5 hover:bg-slate-800"
        >
          {isSidebarOpen ? <ChevronLeft size={20} /> : <Menu size={20} />}
        </button>
      </div>

      <nav className="flex-1 space-y-1 px-3 py-4">
        {navigation.map((item) => {
          const isActive = pathname === item.href;
          return (
            <Link
              key={item.name}
              href={item.href}
              className={cn(
                "flex items-center rounded-lg px-3 py-2.5 transition-colors",
                isActive 
                  ? "bg-indigo-600/10 text-indigo-400" 
                  : "text-slate-400 hover:bg-slate-800 hover:text-slate-100"
              )}
            >
              <item.icon className={cn("h-5 w-5", isActive ? "text-indigo-400" : "")} />
              {isSidebarOpen && (
                <span className="ml-3 text-sm font-medium">{item.name}</span>
              )}
            </Link>
          );
        })}
      </nav>

      <div className="border-t border-slate-800 p-4">
        {isSidebarOpen ? (
          <div className="rounded-xl bg-gradient-to-br from-indigo-600 to-violet-700 p-4">
            <p className="text-xs font-semibold uppercase tracking-wider text-indigo-100">Credits</p>
            <p className="mt-1 text-2xl font-bold">1,240</p>
            <button className="mt-3 w-full rounded-lg bg-white/10 py-1.5 text-xs font-medium hover:bg-white/20">
              Upgrade
            </button>
          </div>
        ) : (
          <div className="flex justify-center">
            <Zap className="h-6 w-6 text-indigo-500" />
          </div>
        )}
      </div>
    </aside>
  );
}