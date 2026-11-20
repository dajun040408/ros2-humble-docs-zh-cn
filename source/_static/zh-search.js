(function () {
  'use strict';

  const aliases = {
    node: ['节点'], nodes: ['节点'],
    topic: ['话题'], topics: ['话题'],
    publisher: ['发布者'], subscriber: ['订阅者'],
    service: ['服务'], services: ['服务'],
    action: ['动作'], actions: ['动作'],
    parameter: ['参数'], parameters: ['参数'],
    executor: ['执行器'], executors: ['执行器'],
    callback: ['回调函数'], 'callback group': ['回调组'],
    lifecycle: ['生命周期'], launch: ['启动文件', '启动系统'],
    qos: ['服务质量', 'QoS'], tf2: ['tf2', '坐标变换'],
    dds: ['DDS'], rmw: ['RMW'], colcon: ['colcon', '工作空间', '功能包']
  };

  function docsBase() {
    const home = document.querySelector('a.icon-home, a[rel="home"]');
    if (home && home.getAttribute('href')) {
      return new URL(home.getAttribute('href'), window.location.href).href.replace(/index\.html?$/, '');
    }
    const path = window.location.pathname;
    const projectMarker = '/ros2-humble-docs-zh-cn/';
    const markerAt = path.indexOf(projectMarker);
    if (markerAt >= 0) return window.location.origin + projectMarker;
    return path.replace(/[^/]*$/, '');
  }

  function escapeHtml(value) {
    return String(value).replace(/[&<>"']/g, ch => ({
      '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'
    })[ch]);
  }

  function queryTerms(query) {
    const normalized = query.toLowerCase().trim();
    const terms = [normalized];
    for (const [english, chinese] of Object.entries(aliases)) {
      if (normalized.includes(english)) terms.push(...chinese.map(x => x.toLowerCase()));
    }
    const cjk = normalized.replace(/[^\u3400-\u9fff]/g, '');
    if (cjk.length > 2) {
      for (let i = 0; i < cjk.length - 1; i++) terms.push(cjk.slice(i, i + 2));
    }
    return [...new Set(terms.filter(Boolean))];
  }

  function installSidebarSearch() {
    document.addEventListener('submit', function (event) {
      const form = event.target;
      if (!(form instanceof HTMLFormElement) || form.id === 'zh-search-form') return;
      const input = form.querySelector('input[name="q"], input[type="search"]');
      if (!input || !input.value.trim()) return;
      event.preventDefault();
      window.location.href = docsBase() + 'search-zh.html?q=' + encodeURIComponent(input.value.trim());
    }, true);
  }

  async function renderSearchPage() {
    const form = document.getElementById('zh-search-form');
    if (!form) return;
    const input = document.getElementById('zh-search-query');
    const meta = document.getElementById('zh-search-meta');
    const results = document.getElementById('zh-search-results');
    const params = new URLSearchParams(window.location.search);
    input.value = params.get('q') || '';

    let index;
    try {
      const response = await fetch(docsBase() + 'search-index.json');
      if (!response.ok) throw new Error('HTTP ' + response.status);
      index = await response.json();
    } catch (error) {
      meta.textContent = '搜索索引暂时不可用，请稍后重试。';
      return;
    }

    function search() {
      const query = input.value.trim();
      results.innerHTML = '';
      if (!query) { meta.textContent = '请输入关键词。'; return; }
      const terms = queryTerms(query);
      const ranked = index.map(item => {
        const title = (item.title || '').toLowerCase();
        const text = (item.text || '').toLowerCase();
        let score = 0;
        if (title.includes(query.toLowerCase())) score += 20;
        if (text.includes(query.toLowerCase())) score += 10;
        for (const term of terms) {
          if (title.includes(term)) score += 5;
          else if (text.includes(term)) score += 1;
        }
        return { item, score };
      }).filter(x => x.score > 0).sort((a, b) => b.score - a.score).slice(0, 50);
      meta.textContent = '找到 ' + ranked.length + ' 条结果';
      if (!ranked.length) {
        results.innerHTML = '<li class="zh-search-empty">没有找到匹配内容。请尝试中文关键词，或使用 Node、Topic、QoS 等英文术语。</li>';
        return;
      }
      for (const result of ranked) {
        const item = result.item;
        const li = document.createElement('li');
        const snippet = (item.text || '').replace(/\s+/g, ' ').slice(0, 220);
        li.innerHTML = '<a href="' + escapeHtml(docsBase() + item.url) + '">' + escapeHtml(item.title) + '</a>' +
          '<div class="zh-search-snippet">' + escapeHtml(snippet) + '</div>';
        results.appendChild(li);
      }
    }
    form.addEventListener('submit', function (event) { event.preventDefault(); search(); });
    if (input.value) search();
  }

  installSidebarSearch();
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', renderSearchPage);
  else renderSearchPage();
})();
