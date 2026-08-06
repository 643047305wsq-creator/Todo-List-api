# Todo List API

基于 FastAPI + SQLAlchemy 实现的待办事项管理接口，支持完整的增删改查功能。

## 功能
- 创建待办事项
- 查询所有待办事项
- 更新待办事项（标题、完成状态）
- 删除待办事项
- 统一的错误处理（404）

## 技术栈
- FastAPI
- SQLAlchemy（ORM）
- SQLite
- Pydantic

## 接口列表
| 方法 | 路径 | 说明 |
|------|------|------|
| POST | /todos/ | 创建待办事项 |
| GET | /todos/ | 查询所有待办事项 |
| PUT | /todo/{todo_id} | 更新指定待办事项 |
| DELETE | /todo/{todo_id} | 删除指定待办事项 |

## 本地运行
\`\`\`bash
pip install fastapi uvicorn sqlalchemy
uvicorn practice:app --reload
\`\`\`
访问 http://127.0.0.1:8000/docs 查看交互式接口文档
