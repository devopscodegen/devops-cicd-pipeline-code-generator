import nextra from 'nextra'

const withNextra = nextra({
  theme: 'nextra-theme-docs',
  themeConfig: './theme.config.tsx',
  latex: true,
  flexsearch: {
    codeblocks: false
  },
  defaultShowCopyCode: true
});

export default withNextra({
  basePath: '/devops-cicd-pipeline-code-generator',
  output: 'export',
  images: {
    unoptimized: true,
  },
  reactStrictMode: true
})
