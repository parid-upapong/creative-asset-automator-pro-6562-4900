"use client";

import { Bell, Search, Plus } from "lucide-react";

export default function Header() {
  return (
    <header className="sticky top-0 z-30 flex h-16 w-full items-center justify-between border-b border-slate-800 bg-slate-950/80 px-4 backdrop-blur-md md:px-8">
      <div className="flex flex-1 items-center">
        <div className="relative w-full max-w-md hidden md:block">
          <Search className="absolute left-3 top-1/2 h-4 w-4 -translate-y-1/2 text-slate-500" />
          <input
            type="text"
            placeholder="Search assets or tasks..."
            className="w-full rounded-full border border-slate-800 bg-slate-900 py-2 pl-10 pr-4 text-sm outline-none focus:ring-2 focus:ring-indigo-500/50"
          />
        </div>
      </div>

      <div className="flex items-center space-x-4">
        <button className="flex items-center space-x-2 rounded-full bg-indigo-600 px-4 py-2 text-sm font-medium transition-hover hover:bg-indigo-500">
          <Plus size={18} />
          <span className="hidden sm:inline">New Project</span>
        </button>
        
        <button className="relative rounded-full border border-slate-800 p-2 text-slate-400 hover:bg-slate-900">
          <Bell size={20} />
          <span className="absolute right-2 top-2 h-2 w-2 rounded-full bg-red-500"></span>
        </button>

        <div className="h-8 w-8 rounded-full bg-gradient-to-tr from-emerald-400 to-cyan-400"></div>
      </div>
    </header>
  );
}